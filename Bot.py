import asyncio
import logging
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import os

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8955476193:AAGcJOMP8FM0cPIbIyxQ4Zs0iLwDyfH-AgA"
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
        "🤖 **Brainrot Farm Mini App!**\n\n"
        "Тапай монеты, открывай кейсы, продавай скины и фарми баланс!\n\n"
        "Нажми кнопку ниже, чтобы запустить игру:"
    )
    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")

async def handle(request):
    return web.Response(text="Bot is running 24/7!")

async def web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

async def main():
    asyncio.create_task(web_server())
    print("=== БОТ УСПЕШНО ЗАПУЩЕН НА RENDER ===")
    await dp.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
# update bot
