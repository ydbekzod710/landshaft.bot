from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Asosiy Menyu
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌲 Manzarali Daraxtlar"), KeyboardButton(text="🏡 Landshaft & Bog' Xizmatlari")],
        [KeyboardButton(text="🪨 Dekorativ Toshlar"), KeyboardButton(text="🖼 Bizning Loyihalar")],
        [KeyboardButton(text="📍 Ko'chatxonamiz Joylashuvi"), KeyboardButton(text="📞 Biz bilan aloqa")]
    ],
    resize_keyboard=True
)

# Landshaft xizmatlari menyusi
services_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌱 Gazon ekish va tayyor gazon"), KeyboardButton(text="✂️ Gazon va daraxtlar strijkasi")],
        [KeyboardButton(text="💉 Dorilash va o'g'itlash"), KeyboardButton(text="📐 Landshaft dizayni")],
        [KeyboardButton(text="⬅️ Orqaga")]
    ],
    resize_keyboard=True
)

# Dekorativ toshlar bo'limi inline tugmalari
stone_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💰 Toshlar Narxlari & Turlari", callback_data="stone_prices")],
        [InlineKeyboardButton(text="🖼 Toshlar bilan Qilingan Dekoratsiyalar", callback_data="stone_decorations")]
    ]
)

# Telefon raqam so'rash tugmasi
phone_req_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)],
        [KeyboardButton(text="⬅️ Orqaga")]
    ],
    resize_keyboard=True
)