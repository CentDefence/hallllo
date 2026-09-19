# -*- coding: utf-8 -*-
"""
Все тексты бота на русском и английском.
Правь смело — это единственное место, где нужно менять контент.
"""

# ==== ССЫЛКИ / КОНТАКТЫ (взято с сайта misteriodesign.vercel.app) ====
OWNER_USERNAME = "mksk5"                 # @mksk5 — контакт / оформление заказа
PORTFOLIO_USERNAME = "portfoliomkskoo"   # @portfoliomkskoo — канал с работами
PRIVACY_URL = "https://telegra.ph/Privacy-09-12-3"

OWNER_URL = f"https://t.me/{OWNER_USERNAME}"
PORTFOLIO_URL = f"https://t.me/{PORTFOLIO_USERNAME}"

# ==== УСЛУГИ (на сайте заявлено "Услуги: 0 из 3", по тэглайну — эти три) ====
SERVICES = {
    "ui": {
        "ru": {"title": "🖥 UI/UX интерфейсы", "desc": "Дизайн интерфейсов сайтов и приложений: от лендинга до полноценного продукта."},
        "en": {"title": "🖥 UI/UX Interfaces", "desc": "Website and app interface design: from a landing page to a full product."},
        "price": 150,
    },
    "visual": {
        "ru": {"title": "🎨 Визуальный дизайн", "desc": "Графика, баннеры, постеры, соцсети — всё, что должно выглядеть эффектно."},
        "en": {"title": "🎨 Visual Design", "desc": "Graphics, banners, posters, social media — everything that needs to look striking."},
        "price": 60,
    },
    "brand": {
        "ru": {"title": "🪪 Айдентика / брендинг", "desc": "Логотип, фирменный стиль, гайдлайн — цельный образ бренда."},
        "en": {"title": "🪪 Identity / Branding", "desc": "Logo, brand style, guidelines — a cohesive brand image."},
        "price": 200,
    },
}

TXT = {
    "ru": {
        "choose_lang": "🌐 Выберите язык / Choose language",
        "welcome": (
            "✨ <b>MISTERIO DESIGN</b>\n"
            "<i>дизайн-услуги</i>\n\n"
            "<u>Диджитал-дизайнер</u>: интерфейсы, визуалы, айдентика.\n"
            "Здесь — портфолио, услуги и оформление заказа в одном месте.\n\n"
            "Выберите раздел ниже 👇"
        ),
        "menu_catalog": "🛍 Каталог услуг",
        "menu_portfolio": "🖼 Портфолио",
        "menu_profile": "👤 Профиль",
        "menu_contacts": "📞 Контакты",
        "menu_order": "🚀 Заказать",
        "switch_lang": "🇬🇧 English",
        "back": "⬅️ Назад",
        "catalog_title": "🛍 <b>Услуги</b>\n<i>Выберите направление:</i>",
        "order_service": "🚀 Заказать эту услугу",
        "profile_title": (
            "👤 <b>Профиль</b>\n\n"
            "<i>Имя:</i> {name}\n"
            "<i>Username:</i> {username}\n"
            "<i>ID:</i> <code>{uid}</code>"
        ),
        "portfolio_title": (
            "🖼 <b>Портфолио</b>\n\n"
            "<i>Более сотни выполненных заказов</i> и постоянные клиенты по всему СНГ.\n"
            "Все работы — в канале ниже."
        ),
        "open_portfolio": "📂 Открыть портфолио",
        "contacts_title": (
            "📞 <b>Контакты и условия</b>\n\n"
            "👤 Связь: {owner}\n"
            "💳 Оплата: <i>Crypto, банки СНГ, бартер</i>\n"
            "📄 Условия: <u>100% предоплата, возврат 50%</u>\n"
        ),
        "privacy": "🔒 Политика конфиденциальности",
        "order_title": (
            "🚀 <b>Заказать</b>\n\n"
            "Нажмите кнопку ниже — откроется чат в Telegram, "
            "где можно обсудить детали и оформить заказ."
        ),
        "help": (
            "<b>Команды бота:</b>\n"
            "/start — начать / выбрать язык заново\n"
            "/menu — главное меню\n"
            "/catalog — каталог услуг\n"
            "/portfolio — портфолио\n"
            "/profile — профиль\n"
            "/order — заказать\n"
            "/help — эта справка\n\n"
            "<i>Команды по умолчанию открываются на русском — переключить язык можно кнопкой в меню.</i>"
        ),
        "not_found": "Не найдено.",
    },
    "en": {
        "choose_lang": "🌐 Choose language / Выберите язык",
        "welcome": (
            "✨ <b>MISTERIO DESIGN</b>\n"
            "<i>design services</i>\n\n"
            "<u>Digital designer</u>: interfaces, visuals, identity.\n"
            "Portfolio, services and checkout — all in one place.\n\n"
           "Choose a section below 👇\n"
 "Link to Misterio Market Web-Site:https://misteriodesign.vercel.app/ 🌐 "
        ),
        "menu_catalog": "🛍 Service catalog",
        "menu_portfolio": "🖼 Portfolio",
        "menu_profile": "👤 Profile",
        "menu_contacts": "📞 Contacts",
        "menu_order": "🚀 Order",
        "switch_lang": "🇷🇺 Русский",
        "back": "⬅️ Back",
        "catalog_title": "🛍 <b>Services</b>\n<i>Choose a category:</i>",
        "order_service": "🚀 Order this service",
        "profile_title": (
            "👤 <b>Profile</b>\n\n"
            "<i>Name:</i> {name}\n"
            "<i>Username:</i> {username}\n"
            "<i>ID:</i> <code>{uid}</code>"
        ),
        "portfolio_title": (
            "🖼 <b>Portfolio</b>\n\n"
            "<i>Over a hundred completed orders</i> and returning clients across the CIS.\n"
            "All the work is in the channel below."
        ),
        "open_portfolio": "📂 Open portfolio",
        "contacts_title": (
            "📞 <b>Contacts & terms</b>\n\n"
            "👤 Contact: {owner}\n"
            "💳 Payment: <i>Crypto, CIS banks, barter</i>\n"
            "📄 Terms: <u>100% prepayment, 50% refund</u>\n"
        ),
        "privacy": "🔒 Privacy policy",
        "order_title": (
            "🚀 <b>Place an order</b>\n\n"
            "Tap the button below to open a Telegram chat "
            "and discuss the details of your order."
        ),
        "help": (
            "<b>Bot commands:</b>\n"
            "/start — start / choose language again\n"
            "/menu — main menu\n"
            "/catalog — service catalog\n"
            "/portfolio — portfolio\n"
            "/profile — profile\n"
            "/order — place an order\n"
            "/help — this help\n\n"
            "<i>Commands default to Russian — switch language with the button in the menu.</i>"
        ),
        "not_found": "Not found.",
    },
}


def t(lang: str, key: str, **kwargs) -> str:
    """Get text by language + key, with optional .format(**kwargs)."""
    lang = lang if lang in TXT else "ru"
    s = TXT[lang].get(key, TXT["ru"].get(key, key))
    return s.format(**kwargs) if kwargs else s
