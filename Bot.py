import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

logging.basicConfig(level=logging.INFO)

# Токен твоего бота
BOT_TOKEN = "8955476193:AAGcJOMP8FM0cPIbIyxQ4Zs0iLwDyfH-AgA"

# Ссылка на твою игру на GitHub Pages
WEB_APP_URL = "https://pbakitkan-hash.github.io/New-agme-2/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🚀 Играть!", web_app=WebAppInfo(url=WEB_APP_URL))]
        ]
    )
    text = (
        "🤖 **Добро пожаловать в Mini App!**\n\n"
        "Тапай монеты, открывай кейсы и выбивай редкие скины прямо в Telegram!\n\n"
        "Нажми кнопку ниже, чтобы открыть игру:"
    )
    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")

async def main():
    print("=== БОТ ЗАПУЩЕН НА RENDER ===")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
