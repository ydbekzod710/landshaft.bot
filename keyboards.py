from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

# Asosiy Menyu (Inline)
main_menu_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌾 Gazon (kg)", callback_data="cat_gazon"),
            InlineKeyboardButton(text="🌲 Manzarali Daraxtlar", callback_data="cat_trees"),
        ],
        [
            InlineKeyboardButton(text="🏡 Landshaft & Bog' Xizmatlari", callback_data="cat_services"),
            InlineKeyboardButton(text="🪨 Dekorativ Toshlar", callback_data="cat_stones"),
        ],
        [
            InlineKeyboardButton(text="🖼 Bizning Loyihalar", callback_data="cat_projects"),
            InlineKeyboardButton(text="🛠 Landshaft uchun narsalar", callback_data="cat_items"),
        ],
        [
            InlineKeyboardButton(text="📍 Ko'chatxonamiz Joylashuvi", callback_data="cat_location"),
            InlineKeyboardButton(text="📞 Biz bilan aloqa", callback_data="cat_contact"),
        ],
    ]
)

# Eski kodlar xatolik bermasligi uchun qoldirildi
main_menu = main_menu_inline
main_menu_kb = main_menu_inline

# Landshaft xizmatlari menyusi (Inline)
services_menu_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌱 Gazon ekish xizmati", callback_data="serv_gazon_ekish"),
            InlineKeyboardButton(text="🟩 Tayyor rulon gazon", callback_data="serv_rulon_gazon"),
        ],
        [
            InlineKeyboardButton(text="✂️ Gazon va daraxtlar strijkasi", callback_data="serv_strijka"),
            InlineKeyboardButton(text="💉 Dorilash va o'g'itlash", callback_data="serv_dorilash"),
        ],
        [
            InlineKeyboardButton(text="📐 Landshaft dizayni", callback_data="serv_dizayn"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_main_inline"),
        ],
    ]
)
services_menu = services_menu_inline

# Dekorativ toshlar asosiy inline menyusi (Ranglar va turlar)
stone_main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔴 Qizil", callback_data="stone_Qizil"),
            InlineKeyboardButton(text="⚪️ Oq", callback_data="stone_Oq"),
        ],
        [
            InlineKeyboardButton(text="🔵 Ko'k", callback_data="stone_Kok"),
            InlineKeyboardButton(text="🟤 Tomircha Qizil", callback_data="stone_TomirchaQizil"),
        ],
        [
            InlineKeyboardButton(text="🟠 Keramzit", callback_data="stone_Keramzit")
        ],
        [
            InlineKeyboardButton(text="🗿 Katta xarsang tosh", callback_data="stone_Xarsang")
        ],
        [
            InlineKeyboardButton(text="🪨 Katta yapaloq tosh", callback_data="stone_Yapaloq")
        ],
        [
            InlineKeyboardButton(text="🖼 Toshlar bilan dekoratsiyalar", callback_data="stone_decorations"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_main_inline")
        ],
    ]
)

# Tosh o'lchamlari menyusi (Kichkina, O'rtacha, Katta)
stone_size_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="▫️ Kichkina (Pista)", callback_data="size_Kichkina")
        ],
        [
            InlineKeyboardButton(text="◽️ O'rtacha (Gugurt)", callback_data="size_Ortacha")
        ],
        [
            InlineKeyboardButton(text="◼️ Katta (Tuxum)", callback_data="size_Katta")
        ],
        [
            InlineKeyboardButton(text="⬅️ Orqaga (Toshlarga)", callback_data="back_to_stones")
        ],
    ]
)

# Katta xarsang toshlar turlari
xarsang_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔹 Katta ko'k tosh", callback_data="buy_xarsang_kok")
        ],
        [
            InlineKeyboardButton(text="🔹 Katta oq tosh", callback_data="buy_xarsang_oq")
        ],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_stones")],
    ]
)

# Katta yapaloq toshlar turlari
yapaloq_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔸 Oq yapaloq", callback_data="buy_yapaloq_oq")
        ],
        [
            InlineKeyboardButton(text="🔸 Ko'k yapaloq", callback_data="buy_yapaloq_kok")
        ],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_stones")],
    ]
)

# Rasm va ma'lumot tagidagi tugma (Faqat Buyurtma berish)
order_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒 Buyurtma berish", callback_data="order_stone")
        ],
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_main_inline")
        ]
    ]
)

# Telefon raqam so'rash tugmasi (Foydalanuvchi kontakt yuborishi uchun pastki klaviatura shart)
phone_req_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)
        ],
        [KeyboardButton(text="⬅️ Orqaga")],
    ],
    resize_keyboard=True,
)

# Landshaft uchun narsalar menyusi (Inline)
landscape_items_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✂️ Qaychi", callback_data="item_qaychi")
        ],
        [
            InlineKeyboardButton(text="📜 Landshaft lenta", callback_data="item_lenta")
        ],
        [
            InlineKeyboardButton(text="🛡 Tosh tagiga material", callback_data="item_material")
        ],
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_main_inline")
        ],
    ]
)

# Gazon kg menyusi (Inline)
gazon_kg_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌱 Sportmaster (1 kg - 100 000 so'm)", callback_data="gazon_sportmaster")
        ],
        [
            InlineKeyboardButton(text="🌱 N1 (1 kg - 100 000 so'm)", callback_data="gazon_n1")
        ],
        [
            InlineKeyboardButton(text="🌱 American Dream (1 kg - 100 000 so'm)", callback_data="gazon_american_dream")
        ],
        [
            InlineKeyboardButton(text="🌱 Fito (1 kg - 100 000 so'm)", callback_data="gazon_fito")
        ],
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_main_inline")
        ],
    ]
)

# Manzarali daraxtlar menyusi (Orqaga tugmasi 'back_to_trees' ga yo'naltiriladi)
tree_items_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌿 Ligustrum piramida", callback_data="tree_ligustrum_pyramid"),
            InlineKeyboardButton(text="🌿 Ionomus piramida", callback_data="tree_euonymus_pyramid"),
        ],
        [
            InlineKeyboardButton(text="🌿 Fatiniya piramida", callback_data="tree_photinia_pyramid"),
            InlineKeyboardButton(text="🌿 Ionomus shtamp katta", callback_data="tree_euonymus_stamba"),
        ],
        [
            InlineKeyboardButton(text="🌿 Arizonika Kiparis primoy", callback_data="tree_arizonica"),
            InlineKeyboardButton(text="🌿 Fatiniya shar", callback_data="tree_photinia_globe"),
        ],
        [
            InlineKeyboardButton(text="🌿 Roza shtamp italy", callback_data="tree_rose_italy"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_main_inline") # 👈 Shu yer o'zgardi
        ],
    ]
)

# Gazonlar uchun maxsus order keyboard (pastki qismida sariqcha emojili tugma bilan)
order_gazon_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒 Buyurtma berish", callback_data="order_stone")
        ],
        [
            InlineKeyboardButton(text="🟠 Orqaga (Gazonlarga)", callback_data="cat_gazon")
        ]
    ]
)






order_item_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Buyurtma berish", callback_data="order_stone")],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_items")]
    ]
)