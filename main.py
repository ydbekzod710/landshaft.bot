import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database import init_db
from handlers import admin, user



async def main():
  logging.basicConfig(level=logging.INFO)
  init_db()

  bot = Bot(token=BOT_TOKEN)
  dp = Dispatcher()

  dp.include_router(user.router)
  dp.include_router(admin.router)

  print("🚀 Bot muvaffaqiyatli ishga tushdi!")
  await dp.start_polling(bot)


if __name__ == "__main__":
  asyncio.run(main())