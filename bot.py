# -*- coding: utf-8 -*-
"""
Локальный запуск для теста (НЕ для продакшена — используй Vercel + webhook).
Запуск: python bot.py
"""
import asyncio
import logging
import os

from dotenv import load_dotenv

from bot_core import create_bot, create_dispatcher

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN", "PUT_YOUR_TOKEN_HERE")

logging.basicConfig(level=logging.INFO)


async def main():
    bot = create_bot(BOT_TOKEN)
    dp = create_dispatcher()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
