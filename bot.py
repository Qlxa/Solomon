import os
import random
import asyncio
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from cards import cards  # імпортуємо список карт з іншого файлу

card = random.choice(cards)

# Формування повідомлення
def format_card_message(card):
    return (
        f"🃏**{card['name']}**\n\n"
        f"✨**Ключові слова:** {card['keywords']}\n\n"
        f"📜**Значення:** {card['meaning']}\n\n"
        f"💡 **Порада дня:** {card['advice']}"
    )

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(
        [[KeyboardButton("Отримати карту дня")]],
        resize_keyboard=True
    )
    await update.message.reply_text(
        "Привіт! Натисни кнопку нижче, щоб отримати карту дня.",
        reply_markup=keyboard
    )

# Відправка випадкової карти
async def send_card(update: Update, context: ContextTypes.DEFAULT_TYPE):
    card = random.choice(cards)
    await update.message.reply_photo(
        photo=card['image'],
        caption=format_card_message(card),
        parse_mode="Markdown"
    )

# Головна функція
def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("Не знайдено токен бота в змінній BOT_TOKEN")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("card", send_card))
    app.add_handler(MessageHandler(filters.Regex("^Отримати карту дня$"), send_card))

    async def run():
        # Видаляємо вебхук і скидаємо старі апдейти перед polling
        await app.bot.delete_webhook(drop_pending_updates=True)
        print("Бот запущений...")
        await app.run_polling(allowed_updates=Update.ALL_TYPES, poll_interval=1.0)

    asyncio.run(run())

if __name__ == "__main__":
    main()
