# -*- coding: utf-8 -*-
"""
Общее ядро бота: создание Bot/Dispatcher и все хендлеры.
Используется:
  - bot.py       — локальный запуск через polling (для разработки/теста)
  - api/webhook.py — обработка через webhook на Vercel (для продакшена)
"""
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from texts import t, SERVICES
import keyboards as kb

DEFAULT_LANG = "ru"  # язык по умолчанию для команд, набранных вручную (/menu, /catalog...)


def create_bot(token: str) -> Bot:
    # parse_mode=HTML — без этого теги <b>, <i> и т.д. показывались бы как
    # обычный текст, а не как форматирование.
    return Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


def create_dispatcher() -> Dispatcher:
    dp = Dispatcher()

    # =========================== /start ===========================
    @dp.message(CommandStart())
    async def cmd_start(message: Message):
        await message.answer(t("ru", "choose_lang"), reply_markup=kb.kb_language())

    @dp.callback_query(F.data.startswith("lang:"))
    async def cb_set_lang(call: CallbackQuery):
        lang = call.data.split(":")[1]
        await call.message.edit_text(t(lang, "welcome"), reply_markup=kb.kb_main_menu(lang))
        await call.answer()

    # =========================== главное меню ===========================
    @dp.message(Command("menu"))
    async def cmd_menu(message: Message):
        await message.answer(t(DEFAULT_LANG, "welcome"), reply_markup=kb.kb_main_menu(DEFAULT_LANG))

    @dp.callback_query(F.data.startswith("menu:"))
    async def cb_menu(call: CallbackQuery):
        _, sub, lang = call.data.split(":")
        if sub == "main":
            await call.message.edit_text(t(lang, "welcome"), reply_markup=kb.kb_main_menu(lang))
        elif sub == "catalog":
            await call.message.edit_text(t(lang, "catalog_title"), reply_markup=kb.kb_catalog(lang))
        elif sub == "portfolio":
            await call.message.edit_text(t(lang, "portfolio_title"), reply_markup=kb.kb_portfolio(lang))
        elif sub == "profile":
            u = call.from_user
            text = t(
                lang, "profile_title",
                name=u.full_name,
                username=f"@{u.username}" if u.username else "—",
                uid=u.id,
            )
            await call.message.edit_text(text, reply_markup=kb.kb_back_main(lang))
        elif sub == "contacts":
            from texts import OWNER_USERNAME
            text = t(lang, "contacts_title", owner=f"@{OWNER_USERNAME}")
            await call.message.edit_text(text, reply_markup=kb.kb_contacts(lang))
        await call.answer()

    # =========================== каталог / услуги ===========================
    @dp.message(Command("catalog"))
    async def cmd_catalog(message: Message):
        await message.answer(t(DEFAULT_LANG, "catalog_title"), reply_markup=kb.kb_catalog(DEFAULT_LANG))

    @dp.callback_query(F.data.startswith("service:"))
    async def cb_service_card(call: CallbackQuery):
        _, key, lang = call.data.split(":")
        item = SERVICES.get(key)
        if not item:
            await call.answer(t(lang, "not_found"), show_alert=True)
            return
        text = f"<b>{item[lang]['title']}</b>\n\n<i>{item[lang]['desc']}</i>\n\n💵 <code>${item['price']}</code>"
        await call.message.edit_text(text, reply_markup=kb.kb_service(lang))
        await call.answer()

    # =========================== профиль ===========================
    @dp.message(Command("profile"))
    async def cmd_profile(message: Message):
        u = message.from_user
        text = t(
            DEFAULT_LANG, "profile_title",
            name=u.full_name,
            username=f"@{u.username}" if u.username else "—",
            uid=u.id,
        )
        await message.answer(text, reply_markup=kb.kb_back_main(DEFAULT_LANG))

    # =========================== портфолио ===========================
    @dp.message(Command("portfolio"))
    async def cmd_portfolio(message: Message):
        await message.answer(t(DEFAULT_LANG, "portfolio_title"), reply_markup=kb.kb_portfolio(DEFAULT_LANG))

    # =========================== заказать ===========================
    @dp.message(Command("order"))
    async def cmd_order(message: Message):
        from texts import OWNER_URL
        await message.answer(t(DEFAULT_LANG, "order_title"), reply_markup=kb.kb_back_main(DEFAULT_LANG))

    # =========================== help ===========================
    @dp.message(Command("help"))
    async def cmd_help(message: Message):
        await message.answer(t(DEFAULT_LANG, "help"))

    return dp
