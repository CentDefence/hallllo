# -*- coding: utf-8 -*-
"""
Точка входа для Vercel. Vercel сам находит переменную `app` (ASGI-приложение)
в файле internal /api/*.py и превращает его в serverless-функцию, доступную
по адресу https://твой-проект.vercel.app/api/webhook

Telegram будет слать сюда POST-запрос с новым сообщением/нажатием кнопки
при каждом обновлении — никакого постоянно висящего процесса не нужно.
"""
import os
import sys

# добавляем корень проекта в путь, чтобы импортировать texts/keyboards/bot_core
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Request
from aiogram.types import Update

from bot_core import create_bot, create_dispatcher

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

app = FastAPI()
bot = create_bot(BOT_TOKEN)
dp = create_dispatcher()


@app.post("/api/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.model_validate(data, context={"bot": bot})
    await dp.feed_update(bot, update)
    return {"ok": True}


@app.get("/api/webhook")
async def health_check():
    # просто чтобы можно было открыть ссылку в браузере и убедиться, что функция жива
    return {"status": "Misterio Design bot is running"}
