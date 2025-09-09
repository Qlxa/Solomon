import os
import random
import logging
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime, timedelta
from telegram import (
    Update, ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice
)
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    ContextTypes, filters, PreCheckoutQueryHandler, CallbackQueryHandler
)
from telegram.error import Forbidden, BadRequest
from cards import cards  # список карт

# ------------------- НАЛАШТУВАННЯ -------------------
trial_period_days = 3         # пробний період у днях
subscription_cost_stars = 100  # вартість підписки у ⭐️
subscription_days = 30         # тривалість підписки у днях
PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN")  # токен для платежів Telegram

# Telegram Stars рахуються у мікроодиницях (1⭐️ = 100_000)
subscription_cost_amount = subscription_cost_stars * 100_000

# ------------------- ЛОГІНГ -------------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ------------------- БАЗА ДАНИХ -------------------
def get_db_connection():
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL environment variable is missing")
    return psycopg2.connect(database_url)

def mark_user_as_blocked(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE subscriptions SET blocked = TRUE WHERE user_id = %s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()

def is_user_blocked(user_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT blocked FROM subscriptions WHERE user_id = %s", (user_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result and result['blocked']

def is_subscription_active(user_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT end_date, blocked FROM subscriptions WHERE user_id = %s", (user_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        if row['blocked']:
            return False
        return datetime.now().date() < row['end_date']
    return False

def give_trial(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=trial_period_days)
    cur.execute("""
        INSERT INTO subscriptions (user_id, start_date, end_date, blocked)
        VALUES (%s, %s, %s, FALSE)
        ON CONFLICT (user_id) DO UPDATE 
        SET start_date = EXCLUDED.start_date, end_date = EXCLUDED.end_date, blocked = FALSE
    """, (user_id, start_date, end_date))
    conn.commit()
    cur.close()
    conn.close()

def activate_subscription(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=subscription_days)
    cur.execute("""
        INSERT INTO subscriptions (user_id, start_date, end_date, blocked)
        VALUES (%s, %s, %s, FALSE)
        ON CONFLICT (user_id) DO UPDATE 
        SET start_date = EXCLUDED.start_date, end_date = EXCLUDED.end_date, blocked = FALSE
    """, (user_id, start_date, end_date))
    conn.commit()
    cur.close()
    conn.close()

# ------------------- ФУНКЦІЇ КЛАВІАТУРИ -------------------
def format_card_message(card):
    return (
        f"🃏**{card['name']}**\n\n"
        f"✨**Ключові слова:** {card['keywords']}\n\n"
        f"📜**Значення:** {card['meaning']}\n\n"
        f"💡 **Порада дня:** {card['advice']}"
    )

def main_keyboard():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("Отримати карту дня", callback_data="get_card")
    ]])

def payment_keyboard():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(text=f"Оплатити {subscription_cost_stars} ⭐️ / {subscription_days} днів", pay=True)
    ]])

async def send_invoice_handler(context, chat_id):
    prices = [LabeledPrice(label=f"Підписка на {subscription_days} днів", amount=subscription_cost_amount)]
    await context.bot.send_invoice(
        chat_id=chat_id,
        title="Підписка на Таро-бота",
        description=f"Доступ до карт Таро протягом {subscription_days} днів",
        payload="subscription_payment",
        provider_token=PROVIDER_TOKEN,
        currency="XTR",
        prices=prices,
        start_parameter="subscription-payment",
        reply_markup=payment_keyboard()
    )

# ------------------- ОБРОБНИКИ -------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if not is_subscription_active(user_id):
        give_trial(user_id)
        await update.message.reply_text(f"Вам надано {trial_period_days} дні безкоштовного користування 🌟")
    else:
        await update.message.reply_text("Ваша підписка активна ✅")

    await update.message.reply_text("Привіт! Натисни кнопку нижче, щоб отримати карту дня.", reply_markup=main_keyboard())

async def send_card(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not is_subscription_active(user_id):
        await update.effective_message.reply_text(
            "⛔ Ваша підписка неактивна.\nНатисніть кнопку нижче для активації:",
            reply_markup=payment_keyboard()
        )
        return

    card = random.choice(cards)
    try:
        await update.effective_message.reply_photo(
            photo=card['image'],
            caption=format_card_message(card),
            parse_mode="Markdown"
        )
    except (Forbidden, BadRequest):
        mark_user_as_blocked(user_id)
        logger.warning(f"Failed to send photo to user {user_id}. Marking as blocked.")
        await update.effective_message.reply_text("Не вдалося надіслати фото. Можливо, бот заблокований вами.")


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "get_card":
        await send_card(update, context)

async def pre_checkout_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.pre_checkout_query
    await query.answer(ok=True)

async def successful_payment_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    activate_subscription(user_id)
    await update.message.reply_text(f"✅ Дякуємо за оплату! Ваша підписка активована на {subscription_days} днів.")

# ------------------- ГОЛОВНА -------------------
def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("Не знайдено BOT_TOKEN")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("card", send_card)) # Залишив цю команду для тестування
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(PreCheckoutQueryHandler(pre_checkout_handler))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_handler))

    logger.info("Бот запущений...")
    app.run_polling()

if __name__ == "__main__":
    main()
