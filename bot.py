import os
import random
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime, timedelta
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters, PreCheckoutQueryHandler
from telegram.error import Forbidden, BadRequest
from cards import cards  # список карт

# ------------------- НАЛАШТУВАННЯ -------------------
trial_period_days = 3   # пробний період у днях
subscription_cost = 100 # вартість підписки у ⭐️
PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN")  # токен для платежів Telegram

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
    start_date = datetime.now()
    end_date = start_date + timedelta(days=trial_period_days)
    cur.execute("""
        INSERT INTO subscriptions (user_id, start_date, end_date, blocked)
        VALUES (%s, %s, %s, FALSE)
        ON CONFLICT (user_id) DO UPDATE 
        SET start_date = EXCLUDED.start_date, end_date = EXCLUDED.end_date, blocked = FALSE
    """, (user_id, start_date.date(), end_date.date()))
    conn.commit()
    cur.close()
    conn.close()

# ------------------- ФУНКЦІЇ -------------------
def format_card_message(card):
    return (
        f"🃏**{card['name']}**\n\n"
        f"✨**Ключові слова:** {card['keywords']}\n\n"
        f"📜**Значення:** {card['meaning']}\n\n"
        f"💡 **Порада дня:** {card['advice']}"
    )

def payment_keyboard():
    return InlineKeyboardMarkup([[InlineKeyboardButton(text="Оплатити 100 ⭐️ / 30 днів", pay=True)]])

async def send_invoice_handler(context, chat_id):
    prices = [LabeledPrice(label="Підписка на 30 днів", amount=subscription_cost)]
    await context.bot.send_invoice(
        chat_id=chat_id,
        title="Підписка на Таро-бота",
        description="Доступ до карт Таро протягом 30 днів",
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
        await update.message.reply_text("Вам надано 3 дні безкоштовного користування 🌟")
    else:
        await update.message.reply_text("Ваша підписка активна ✅")

    keyboard = ReplyKeyboardMarkup([[KeyboardButton("Отримати карту дня")]], resize_keyboard=True)
    await update.message.reply_text("Привіт! Натисни кнопку нижче, щоб отримати карту дня.", reply_markup=keyboard)

async def send_card(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if not is_subscription_active(user_id):
        await update.message.reply_text("⛔ Ваша підписка неактивна. Потрібно оформити донат.")
        await send_invoice_handler(context, update.message.chat_id)
        return

    card = random.choice(cards)
    try:
        await update.message.reply_photo(
            photo=card['image'],
            caption=format_card_message(card),
            parse_mode="Markdown"
        )
    except Forbidden:
        mark_user_as_blocked(user_id)

async def pre_checkout_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.pre_checkout_query
    await query.answer(ok=True)

async def successful_payment_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    start_date = datetime.now()
    end_date = start_date + timedelta(days=30)
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO subscriptions (user_id, start_date, end_date, blocked)
        VALUES (%s, %s, %s, FALSE)
        ON CONFLICT (user_id) DO UPDATE 
        SET start_date = EXCLUDED.start_date, end_date = EXCLUDED.end_date, blocked = FALSE
    """, (user_id, start_date, end_date))
    conn.commit()
    cur.close()
    conn.close()
    await update.message.reply_text("✅ Дякуємо за оплату! Ваша підписка активована на 30 днів.")

# ------------------- ГОЛОВНА -------------------
def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("Не знайдено BOT_TOKEN")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("card", send_card))
    app.add_handler(MessageHandler(filters.Regex("^Отримати карту дня$"), send_card))
    app.add_handler(PreCheckoutQueryHandler(pre_checkout_handler))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_handler))

    print("Бот запущений...")
    app.run_polling()

if __name__ == "__main__":
    main()
