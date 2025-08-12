import os
import random
import re
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from telegram.constants import ParseMode
from cards import cards  # імпортуємо список карт з іншого файлу

# Функція для екранування спецсимволів MarkdownV2
def escape_markdown(text: str) -> str:
    return re.sub(r'([_*\[\]()~`>#+\-=|{}.!])', r'\\\1', text)

# Формування повідомлення
def format_card_message(card):
    return (
        f"🎴\n\n"
        f"*{escape_markdown(card['name'])}*\n\n"
        f"✨ *Ключові слова:* {escape_markdown(card['keywords'])}\n\n"
        f"📜 *Значення:* {escape_markdown(card['meaning'])}\n\n"
        f"💡 *Порада дня:* {escape_markdown(card['advice'])}"
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
        parse_mode=ParseMode.MARKDOWN_V2
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

    print("Бот запущений...")
    app.run_polling()

if __name__ == "__main__":
    main()
