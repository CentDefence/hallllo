# -*- coding: utf-8 -*-
"""
Запусти ОДИН РАЗ после того, как задеплоил проект на Vercel, чтобы сказать
Telegram: "присылай обновления сюда".

Использование:
    python set_webhook.py https://твой-проект.vercel.app

(токен бота берётся из .env, см. .env.example)
"""
import asyncio
import os
import sys

from dotenv import load_dotenv
from aiogram import Bot

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN", "")


async def main():
    if len(sys.argv) < 2:
        print("Использование: python set_webhook.py https://твой-проект.vercel.app")
        return
    base_url = sys.argv[1].rstrip("/")
    webhook_url = f"{base_url}/api/webhook"

    bot = Bot(token=BOT_TOKEN)
    await bot.set_webhook(webhook_url)
    info = await bot.get_webhook_info()
    print(f"✅ Webhook установлен: {webhook_url}")
    print(info)
    await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
