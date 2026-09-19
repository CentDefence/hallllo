# -*- coding: utf-8 -*-
"""
Все callback_data имеют вид "действие:параметр:язык" — например "menu:catalog:ru".
Так язык "путешествует" внутри самих кнопок, и боту не нужно ничего запоминать
между запросами — это обязательно для serverless (Vercel не хранит память
между вызовами функции).
"""
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from texts import t, SERVICES, OWNER_URL, PORTFOLIO_URL, PRIVACY_URL


def kb_language() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="🇷🇺 Русский", callback_data="lang:ru")
    b.button(text="🇬🇧 English", callback_data="lang:en")
    b.adjust(2)
    return b.as_markup()


def kb_main_menu(lang: str) -> InlineKeyboardMarkup:
    other = "en" if lang == "ru" else "ru"
    b = InlineKeyboardBuilder()
    b.button(text=t(lang, "menu_catalog"), callback_data=f"menu:catalog:{lang}")
    b.button(text=t(lang, "menu_portfolio"), callback_data=f"menu:portfolio:{lang}")
    b.button(text=t(lang, "menu_profile"), callback_data=f"menu:profile:{lang}")
    b.button(text=t(lang, "menu_contacts"), callback_data=f"menu:contacts:{lang}")
    b.button(text=t(lang, "menu_order"), url=OWNER_URL)          # прямая ссылка — 1 клик в Telegram
    b.button(text=t(lang, "switch_lang"), callback_data=f"lang:{other}")
    b.adjust(2, 2, 1, 1)
    return b.as_markup()


def kb_back_main(lang: str) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text=t(lang, "back"), callback_data=f"menu:main:{lang}")
    return b.as_markup()


def kb_catalog(lang: str) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    for key, item in SERVICES.items():
        b.button(text=item[lang]["title"], callback_data=f"service:{key}:{lang}")
    b.button(text=t(lang, "back"), callback_data=f"menu:main:{lang}")
    b.adjust(1)
    return b.as_markup()


def kb_service(lang: str) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text=t(lang, "order_service"), url=OWNER_URL)
    b.button(text=t(lang, "back"), callback_data=f"menu:catalog:{lang}")
    b.adjust(1)
    return b.as_markup()


def kb_portfolio(lang: str) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text=t(lang, "open_portfolio"), url=PORTFOLIO_URL)
    b.button(text=t(lang, "back"), callback_data=f"menu:main:{lang}")
    b.adjust(1)
    return b.as_markup()


def kb_contacts(lang: str) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text=t(lang, "privacy"), url=PRIVACY_URL)
    b.button(text=t(lang, "back"), callback_data=f"menu:main:{lang}")
    b.adjust(1)
    return b.as_markup()
