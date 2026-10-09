import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Твой токен бота
TOKEN = "8955476193:AAGcJOMP8FM0cPIbIyxQ4Zs0iLwDyfH-AgA"

# Инициализируем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Твой Telegram Mini App кликер успешно запущен на Render! 🚀\n"
        "Можешь открывать приложение."
    )

# Функция запуска бота
async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    
    # Очищаем старые апдейты перед запуском
    await bot.delete_webhook(drop_pending_updates=True)
    
    print("=== БОТ УСПЕШНО ЗАПУЩЕН НА RENDER ===")
    
    # Запускаем поллинг
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
