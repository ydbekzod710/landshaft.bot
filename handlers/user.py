import sqlite3
from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    BotCommand,
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ReplyKeyboardRemove,
)
from config import ADMIN_IDS, LOCATION_LAT, LOCATION_LON, LOCATION_TEXT
from keyboards import (
    gazon_kg_menu_kb,
    landscape_items_kb,
    main_menu_kb,
    order_gazon_inline_kb,
    order_inline_kb,
    order_item_kb,
    phone_req_kb,
    services_menu,
    stone_main_kb,
    stone_size_kb,
    tree_items_kb,
    xarsang_kb,
    yapaloq_kb,
)

router = Router()

# === RASM ID VA MATNNI SHU YERDAN O'ZGARTIRASIZ ===
RESTART_PHOTO_ID = "AgACAgIAAxkBAAIHZ2rTHVkmkiq12ZtPcm9gSutr187YAAJ3J2sbFEKQSoCwf_vEC341AQADAgADeAADPQQ"
RESTART_CAPTION = (
    "👋 **Assalomu alaykum! Landshaft dizayn botiga xush kelibsiz.**\n\n"
    "Quyidagi bo'limlardan birini tanlang:"
)


class Form(StatesGroup):
    waiting_for_phone = State()
    waiting_for_m2 = State()
    waiting_for_kg = State()

# === GURUHGA YUBORUVCHI YAGONA FUNKSIYA ===
async def send_to_group(bot, user, text_content, phone=None):
    username = f"@{user.username}" if user.username else "Mavjud emas"
    phone_str = f"+{phone}" if phone else "Yuborilmagan"

    msg = (
        f"📩 **YANGI BUYURTMA QABUL QILINDI!**\n\n"
        f"👤 **Mijoz ismi:** {user.full_name}\n"
        f"🔗 **Username (Niki):** {username}\n"
        f"🆔 **Telegram ID:** `{user.id}`\n"
        f"📞 **Telefon raqami:** {phone_str}\n\n"
        f"{text_content}"
    )
    try:
        await bot.send_message(
            chat_id=-1004438519748, text=msg, parse_mode="Markdown"
        )
    except Exception as e:
        print(f"Guruhga yuborishda xatolik: {e}")


# Start va Restart buyruqlari
@router.message(CommandStart())
@router.message(Command("restart"))
async def start_cmd(message: Message, state: FSMContext):
    await state.clear()

    # Pastda qolib ketgan oddiy Reply-klaviaturalarni o'chirib tashlaymiz
    try:
        remove_msg = await message.answer("...", reply_markup=ReplyKeyboardRemove())
        await remove_msg.delete()
    except Exception:
        pass

    # 1. Avval rasmni va uning tagidagi matnni (caption) yuboramiz
    if RESTART_PHOTO_ID:
        try:
            await message.answer_photo(
                photo=RESTART_PHOTO_ID,
                caption=RESTART_CAPTION,
                parse_mode="Markdown",
            )
        except Exception as e:
            print(f"Rasm yuborishda xatolik: {e}")
            await message.answer(
                RESTART_CAPTION,
                parse_mode="Markdown",
            )
    else:
        await message.answer(
            RESTART_CAPTION,
            parse_mode="Markdown",
        )

    # 2. Tugmalar panelini eng pastda alohida xabar qilib chiqaramiz
    await message.answer(
        "Quyidagi bo'limlardan birini tanlang:",
        reply_markup=main_menu_kb,
        parse_mode="Markdown",
    )

# Asosiy menyuga qaytish
@router.callback_query(F.data == "back_to_main_inline")
async def back_to_main_inline_handler(call: CallbackQuery, state: FSMContext):
    await state.clear()
    text = "👋 **Assalomu alaykum! Landshaft dizayn botiga xush kelibsiz.**"

    try:
        await call.message.delete()
    except Exception:
        pass

    await call.message.answer(
        text, reply_markup=main_menu_kb, parse_mode="Markdown"
    )
    await call.answer()


@router.message(F.text == "⬅️ Orqaga")
async def back_cmd(message: Message, state: FSMContext):
    await state.clear()
    text = "👋 **Assalomu alaykum! Landshaft dizayn botiga xush kelibsiz.**\n\nKerakli bo'limni tanlang:"
    
    await message.answer("...", reply_markup=ReplyKeyboardRemove())
    await message.answer(text, reply_markup=main_menu_kb, parse_mode="Markdown")


# === BIZNING LOYIHALAR ===
PORTFOLIO_ITEMS = [
    {
        "title": "📁 1-Loyiha",
        "video": "BAACAgQAAxkBAAPVas-kgUhBWVdoNOpzF8lNERzW3ZgAAnMMAAJu74RSJ9f8gXy5Z3U9BA",
        "caption": "🎬 **1-Loyihamiz\n**• Biz bu loyihamizda:\n•Tayyor gazon\n•Landshaftli Dizayn\n•Italyadan keltirilgan daraxtlar ekib berdik\n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 2-Loyiha",
        "video": "BAACAgQAAxkBAAPTas-keB57EYWyScduVzIpFc9STioAAkwMAAJJvXxSsFA7vIZmzgs9BA",
        "caption": "🎬 **2-Loyihamiz\n**• Biz bu loyihamizda:\n•Tayyor gazon\n•Dekorativ toshlar\n•Dekorativ Kara(Daraxt po'sloqi)\n•Italyadan keltirilgan daraxtlar bilan minimalistik dizayn  \n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 3-Loyiha",
        "video": "BAACAgQAAxkBAAPRas-kG2mapIU8z72y15HqW7aV3tEAAmwMAAIanH1SH_52ccR6Mng9BA",
        "caption": "🎬 **3-Loyihamiz\n**• Biz bu loyihamizda:\n•Tayyor gazon \n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 4-Loyiha",
        "video": "BAACAgQAAxkBAAPPas-kClnG013chp2uMpeuoWkxc0wAAjcMAALvfoRSU6DtV-m8epU9BA",
        "caption": "🎬 **4-Loyihamiz\n**• Biz bu loyihamizda:\n•Tayyor gazon\n•Italyadan keltirilgan daraxt 'Fatinya' bilan minimalistik dizayn  \n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 5-Loyiha",
        "video": "BAACAgIAAxkBAAPNas-j55rUJp2uffUvyKBebN1R4e0AAsV_AAJZfYlKX9yQN1bv9Z09BA",
        "caption": "🎬 **5-Loyihamiz\n**• Biz bu loyihamizda:\n•Tayyor gazon\n•Dekorativ o'rmashuvchan ko'chat \n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 6-Loyiha",
        "video": "BAACAgQAAxkBAAPLas-jtLIetvTB4GaLKkqcLk9had8AAjsKAAKur6VRiQ27Aqqh-IE9BA",
        "caption": "🎬 **6-Loyihamiz\n**• Biz bu loyihamizda:\nEski qurigan gazonni qirib o'rniga:\n•Tayyor gazon\n•Italyadan keltirilgan daraxtlar bilan minimalistik dizayn qilib berdik \n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 7-Loyiha",
        "video": "BAACAgQAAxkBAAPJas-jn3ng98cznTfnOTTQeXQi8AwAAlIKAALIXj1ScZt2uHHmQvQ9BA",
        "caption": "🎬 **7-Loyihamiz\n**• Biz bu loyihamizda:\n •Gazon ekib bergan edik\n•Italyadan keltirilgan daraxtlar bilan minimalistik dizayn  \n•Strijka xizmati\n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 8-Loyiha",
        "video": "BAACAgIAAxkBAAPHas-jkCMyuDURLr3yra0H3CpLfxcAAoWpAAJpSXhK3Tc-x-kfXD09BA",
        "caption": "🎬 **8-Loyihamiz\n**• Biz bu loyihamizda:\n •Eski qurigan gazonni o'rniga yangi Gazon ekib berdik\n•Eski dizaynga yana gul va daraxtlar qoshib yanada chiroyli qildik\n•Drinaj xizmati(o'ta kuchli namlikni qaytaradi)\n•Italyadan keltirilgan daraxtlar bilan minimalistik dizayn  \n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 9-Loyiha",
        "video": "BAACAgIAAxkBAAPFas-jcqU2yGGq0wo4anwrw-SlWKIAAoSpAAJpSXhKmJclsOonlio9BA",
        "caption": "🎬 **9-Loyihamiz\n**• Biz bu loyihamizda:\n•Tayyor gazon\n•Dekorativ toshlar\n•Dekorativ Kara(Daraxt po'sloqi)\n•Italyadan keltirilgan daraxtlar bilan zich dizayn  \n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 10-Loyiha",
        "video": "BAACAgQAAxkBAAPDas-jZDyhLBUHzVwm7Qu2ul417ecAAh4MAAIcjoRSET74Na1Kf9Y9BA",
        "caption": "🎬 **10-Loyihamiz\n**• Biz bu loyihamizda:\n•Gazon ekib berdik\n•Italyadan keltirilgan daraxtlar bilan maksimalistik dizayn  \n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 11-Loyiha",
        "video": "BAACAgQAAxkBAAO_as-jP0f_4UrEA8nybbFkx9uWFQ4AArsMAAL5tnxSG1Zz2xowGZs9BA",
        "caption": "🎬 **11-Loyihamiz\n**• Biz bu loyihamizda:\n•Tayyor gazon\n•Italyadan keltirilgan daraxtlar bilan dizayn  \n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 12-Loyiha",
        "video": "BAACAgIAAxkBAAO9as-jNoehalwpNiFGSU6iYYy18HQAAlKrAAIaHBhLnRQJy3Byh4k9BA",
        "caption": "🎬 **12-Loyihamiz\n**• Biz bu loyihamizda:\n•Tayyor gazon\n•Dekorativ toshlar\n•Italyadan keltirilgan daraxtlar bilan dizayn\n•O'zb daraxlatlaridan:Palma,Fatinya mesni  \n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 13-Loyiha",
        "video": "BAACAgIAAxkBAAO7as-jLz8v9tm3mJtRVhDIkaUCGYUAAoKpAAJpSXhK-qnEiTXZBQk9BA",
        "caption": "🎬 **13-Loyihamiz\n**• Biz bu loyihamizda:\n•Tayyor gazon\n•Dekorativ toshlar\n•Dekorativ Kara(Daraxt po'sloqi)\n•Dorilab berdik(Daraxt po'sloqi)\n•Italyadan keltirilgan daraxtlar bilan maksimalistik dizayn  \n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 14-Loyiha",
        "video": "BAACAgIAAxkBAAO5as-jFTYC1ESrJb4ieuWdIRtiqiEAAn-pAAJpSXhKrALoH3rP9M49BA",
        "caption": "🎬 **14-Loyihamiz\n**• Biz bu loyihamizda:\n•Gazon ekib berdik\n•Italyadan keltirilgan daraxtlar bilan maksimalistik dizayn\n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 15-Loyiha",
        "video": "BAACAgIAAxkBAAO3as-jBZbiKst9HikacvizYYf1XckAAnypAAJpSXhKcVvwYrOiL9g9BA",
        "caption": "🎬 **15-Loyihamiz\n**• Biz bu loyihamizda:\n•Tayyor gazon\n•Dorilab berdik\n•Italyadan keltirilgan daraxtlar bilan maksimalistik dizayn\n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 16-Loyiha",
        "video": "BAACAgIAAxkBAAOzas-i5fVPXCb-mM-BcUYIDy_5TQQAAnipAAJpSXhKChOEzJJEOX49BA",
        "caption": "🎬 **16-Loyihamiz\n**• Biz bu loyihamizda:\n•To'laqonli Toshlar bilan dekoratsiya\n•Kara(daraxt po'stloqi) bilan dizayn\n•Eski dizaynga yanada ko'proq Dizayn qoshildi\n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 17-Loyiha",
        "video": "BAACAgQAAxkBAAOxas-ixRcd9edRR8tv43REOklDmq4AAjkMAAL5qIVSuzcw0cXL3Bo9BA",
        "caption": "🎬 **17-Loyihamiz\n**• Biz bu loyihamizda:\n•To'laqonli Toshlar bilan dekoratsiya\n•Kara(daraxt po'stloqi) bilan dizayn\n•Italyadan keltirilgan daraxtlar \n•Kombinatsion Dizayn\n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 18-Loyiha",
        "video": "BAACAgQAAxkBAAOvas-iwEhgNimFQdGPsFmdKGekbTcAAjoMAAL36YRSjbVkC8GybzY9BA",
        "caption": "🎬 **18-Loyihamiz\n**• Biz bu loyihamizda:\n•Tayyor gazon\n•Dorilab berdik\n•Italyadan keltirilgan daraxtlar bilan o'rtacha dizayn\n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 19-Loyiha",
        "video": "BAACAgQAAxkBAAOtas-ihG-jlkUlY7TWUG-SgF48w48AAjIMAAL1YYRSKfxtv4bsZXs9BA",
        "caption": "🎬 **19-Loyihamiz\n**• Biz bu loyihamizda:\n•Tayyor gazon\n•Dorilab berdik\n•Kara(daraxt po'stloqi)bilan dekoratsiya\n•Italyadan keltirilgan daraxtlar bilan o'rtacha dizayn\n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 20-Loyiha",
        "video": "BAACAgIAAxkBAAOras-ieKm_6LI_itaKDciOEmedcFAAAnapAAJpSXhK9bwF4hArDkg9BA",
        "caption": "🎬 **20-Loyihamiz\n**• Biz bu loyihamizda:\n•Landshaftli Dizayn\n•Italyadan keltirilgan daraxtlar ekib berdik\n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 21-Loyiha",
        "video": "BAACAgIAAxkBAAOpas-iXomQjBtAo4krKejY842Zo10AAiKpAAJpSXhKTj2bcDzi6cM9BA",
        "caption": "🎬 **21-Loyihamiz\n**• Biz bu loyihamizda:\n•Landshaftli Dizayn\n•Italyadan keltirilgan daraxtlar ekib berdik\n•Kombinatsion dekoratsiya\n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
    {
        "title": "📁 22-Loyiha",
        "video": "BAACAgIAAxkBAAOnas-iTF_W0FF3xGgUHtnRxhq9p44AAqGoAAIDjghKDY504tq7jgABPQQ",
        "caption": "🎬 **22-Loyihamiz\n**• Biz bu loyihamizda:\n•Tayyor gazon\n•Dorilab berdik\n•Italyadan keltirilgan daraxtlar bilan dizayn\n\n📞 **Murojaat uchun:** +998-93-722-41-11",
    },
]


@router.callback_query(F.data == "cat_projects")
async def show_portfolio(call: CallbackQuery):
    keyboard_buttons = []
    row = []
    for idx, item in enumerate(PORTFOLIO_ITEMS):
        row.append(
            InlineKeyboardButton(
                text=item["title"], callback_data=f"project_{idx}"
            )
        )
        if len(row) == 2:
            keyboard_buttons.append(row)
            row = []
    if row:
        keyboard_buttons.append(row)

    keyboard_buttons.append(
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_main_inline")]
    )

    markup = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
    text = "🎬 **Bizning bajarilgan landshaft loyihalarimiz!**\n\nQuyidagi loyihalardan birini tanlang va videoni tomosha qiling:"

    try:
        await call.message.delete()
    except Exception:
        pass

    await call.message.answer(
        text, reply_markup=markup, parse_mode="Markdown"
    )
    await call.message.answer(
        "Quyidagi bo'limlardan birini tanlang:",
        reply_markup=main_menu_kb,
        parse_mode="Markdown"
    )
    await call.answer()


@router.callback_query(F.data.startswith("project_"))
async def show_selected_project(callback: CallbackQuery):
    idx = int(callback.data.split("_")[1])
    item = PORTFOLIO_ITEMS[idx]

    try:
        await callback.message.delete()
    except Exception:
        pass

    await callback.message.answer_video(
        video=item["video"], 
        caption=item["caption"], 
        parse_mode="Markdown"
    )
    await callback.message.answer(
        "Quyidagi bo'limlardan birini tanlang:",
        reply_markup=main_menu_kb,
        parse_mode="Markdown"
    )
    await callback.answer()


# === LANDSHAFT UCHUN NARSALAR ===
@router.callback_query(F.data == "cat_items")
async def landscape_items_section(call: CallbackQuery):
    text = (
        "🛠 **Landshaft uchun kerakli mahsulotlar bo'limiga xush kelibsiz!**\n\n"
        "Kerakli mahsulotni tanlang:"
    )
    try:
        await call.message.delete()
    except Exception:
        pass

    await call.message.answer(
        text, reply_markup=landscape_items_kb, parse_mode="Markdown"
    )
    await call.answer()


@router.callback_query(F.data == "item_qaychi")
async def show_qaychi(call: CallbackQuery, state: FSMContext):
    await state.update_data(stone_name="Bog' qaychisi", price_text="44 000 so'm")
    text = (
        "✂️ **Bog' qaychisi**\n\n"
        "💰 **Narxi:** 44 000 so'm\n\n"
        "Buyurtma berish uchun pastdagi tugmani bosing:"
    )
    try:
        await call.message.delete()
    except Exception:
        pass

    await call.message.answer(
        text, reply_markup=order_item_kb, parse_mode="Markdown"
    )
    await call.answer()


@router.callback_query(F.data == "item_lenta")
async def show_lenta(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        stone_name="Landshaft lenta", price_text="250 000 so'm / 1 rulon"
    )
    text = (
        "📜 **Landshaft lenta**\n\n"
        "📏 **O'lchami:** 1 ta rulon\n"
        "💰 **Narxi:** 250 000 so'm\n\n"
        "Buyurtma berish uchun pastdagi tugmani bosing:"
    )
    try:
        await call.message.delete()
    except Exception:
        pass

    await call.message.answer(
        text, reply_markup=order_item_kb, parse_mode="Markdown"
    )
    await call.answer()


@router.callback_query(F.data == "item_material")
async def show_material(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        stone_name="Tosh tagiga material", price_text="12 000 so'm / 1 m"
    )
    text = (
        "🛡 **Tosh tagiga material (Geoteksil)**\n\n"
        "📏 **O'lchami:** 1 metr (m)\n"
        "💰 **Narxi:** 12 000 so'm\n\n"
        "Buyurtma berish uchun pastdagi tugmani bosing:"
    )
    try:
        await call.message.delete()
    except Exception:
        pass

    await call.message.answer(
        text, reply_markup=order_item_kb, parse_mode="Markdown"
    )
    await call.answer()


@router.callback_query(F.data == "back_to_items")
async def back_to_items_handler(call: CallbackQuery):
    text = (
        "🛠 **Landshaft uchun kerakli mahsulotlar bo'limiga xush kelibsiz!**\n\n"
        "Kerakli mahsulotni tanlang:"
    )
    try:
        await call.message.delete()
    except Exception:
        pass

    await call.message.answer(
        text, reply_markup=landscape_items_kb, parse_mode="Markdown"
    )
    await call.answer()


# === LANDSHAFT & BOG' XIZMATLARI ===
@router.callback_query(F.data == "cat_services")
async def landscape_section(call: CallbackQuery):
    text = "Kerakli xizmat turini tanlang:"
    try:
        await call.message.delete()
    except Exception:
        pass

    await call.message.answer(
        text, reply_markup=services_menu, parse_mode="Markdown"
    )
    await call.answer()


@router.callback_query(F.data == "serv_strijka")
async def strijka_service(call: CallbackQuery):
    text = (
        "✂️ **Gazon va daraxtlar strijkasi**\n\n"
        "Joyning kattaligi va daraxtlar soniga qarab narxi kelishiladi.\n\n"
        "📞 **Murojaat uchun raqamlar:**\n+998-93-722-41-11, +998-93-729-11-41\n\n"
        "💬 **Telegram:** @Baxodir4111"
    )
    try:
        await call.message.delete()
    except Exception:
        pass
    await call.message.answer(text, reply_markup=main_menu_kb, parse_mode="Markdown")
    await call.answer()


@router.callback_query(F.data == "serv_dorilash")
async def dorilash_service(call: CallbackQuery):
    text = (
        "💉 **Dorilash va o'g'itlash xizmati**\n\n"
        "Joyning kattaligi va daraxtlar soniga qarab narxi kelishiladi.\n\n"
        "📞 **Murojaat uchun raqamlar:**\n+998-93-722-41-11, +998-93-729-11-41\n\n"
        "💬 **Telegram:** @Baxodir4111"
    )
    try:
        await call.message.delete()
    except Exception:
        pass
    await call.message.answer(text, reply_markup=main_menu_kb, parse_mode="Markdown")
    await call.answer()


@router.callback_query(F.data == "serv_dizayn")
async def landscape_design_service(call: CallbackQuery):
    text = (
        "📐 **Landshaft dizayni xizmati**\n\n"
        "Bizda tosh, gazon hamda daraxtlar bilan qilinadigan professional landshaft dizaynlar mavjud. "
        "Hovlingizni eng so'nggi uslubda ko'kalamzorlashtirib beramiz!\n\n"
        "📞 **Murojaat uchun raqamlar:**\n+998-93-722-41-11, +998-94-994-00-07\n\n"
        "💬 **Telegram:** @Baxodir4111"
    )
    try:
        await call.message.delete()
    except Exception:
        pass
    await call.message.answer(text, reply_markup=main_menu_kb, parse_mode="Markdown")
    await call.answer()


@router.callback_query(F.data == "serv_gazon_ekish")
async def start_calc_seed(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        service_name="Gazon ekish xizmati", price_per_m2=45000
    )
    try:
        await call.message.delete()
    except Exception:
        pass
    await call.message.answer(
        "🌱 Gazon ekish xizmati tanlandi (40k - 50k / m²).\n\n"
        "📐 Necha m² (kvadrat metr) maydon uchun hisoblaymiz?\nIltimos, faqat raqam kiriting (Masalan: 150):"
    )
    await state.set_state(Form.waiting_for_m2)
    await call.answer()


@router.callback_query(F.data == "serv_rulon_gazon")
async def start_calc_roll(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        service_name="Tayyor rulon gazon", price_per_m2=90000
    )
    try:
        await call.message.delete()
    except Exception:
        pass
    await call.message.answer(
        "🟩 Tayyor rulon gazon tanlandi (80k - 100k / m²).\n\n"
        "📐 Necha m² (kvadrat metr) maydon uchun hisoblaymiz?\nIltimos, faqat raqam kiriting (Masalan: 150):"
    )
    await state.set_state(Form.waiting_for_m2)
    await call.answer()


@router.message(Form.waiting_for_m2)
async def process_m2(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Iltimos, faqat musbat raqam yozing (masalan: 150):")
        return

    m2 = int(message.text)
    data = await state.get_data()

    service_name = data.get("service_name")
    price_per_m2 = data.get("price_per_m2")

    total = m2 * price_per_m2
    formatted_total = f"{total:,}".replace(",", " ")
    formatted_price_per_m2 = f"{price_per_m2:,}".replace(",", " ")

    await state.update_data(m2=m2, total=formatted_total)

    text = (
        f"🛠 Xizmat: {service_name}\n"
        f"📐 Maydon: {m2} m²\n"
        f"💵 1 m² narxi: {formatted_price_per_m2} so'm\n"
        f"💰 Jami taxminiy qiymat: {formatted_total} so'm\n\n"
        "Buyurtma berish uchun telefon raqamingizni yuboring:"
    )
    await message.answer(text, reply_markup=phone_req_kb, parse_mode="Markdown")
    await state.set_state(Form.waiting_for_phone)


# === GAZON (KG) ===
@router.callback_query(F.data == "cat_gazon")
async def main_gazon_kg_menu(call: CallbackQuery):
    text = (
        "🌾 **Gazon urug'lari bo'limi (Kilogrammda)**\n\n"
        "Kerakli gazon turini tanlang:"
    )
    try:
        await call.message.delete()
    except Exception:
        pass

    await call.message.answer(
        text, reply_markup=gazon_kg_menu_kb, parse_mode="Markdown"
    )
    await call.answer()


@router.callback_query(F.data.startswith("gazon_"))
async def show_gazon_details(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
    except Exception:
        pass
    await call.answer()

    gazon_info = {
        "gazon_sportmaster": {
            "name": "Sportmaster gazon (kg)",
            "photo": "AgACAgIAAxkBAAIDYWrR9sfMOmyIaCaboa8Hs5V0zEAsAAL-ImsbxW2RSvFetV6Ych_5AQADAgADeAADPQQ",
            "desc": "Qattiq qadamlarga juda chidamli, sport maydonchalari va faol hovlilar uchun mo'ljallangan mustahkam gazon turi.",
        },
        "gazon_n1": {
            "name": "N1 gazon (kg)",
            "photo": "AgACAgIAAxkBAAIDZWrR9wV09xkrPOmh7ykpKSEEo8aMAAIPI2sbxW2RSiUnvy1kDv18AQADAgADeAADPQQ",
            "desc": "Universzal va tez unib chiquvchi yuqori sifatli gazon turi.",
        },
        "gazon_american_dream": {
            "name": "American Dream gazon (kg)",
            "photo": "AgACAgIAAxkBAAIDY2rR9wE1Vl3KHZ9lHL6H11s-dyoqAAIOI2sbxW2RSrCE8KNH1BsqAQADAgADeQADPQQ",
            "desc": "Yorqin yashil rangga ega, maysasi yumshoq va juda ko'rkam manzarali gazon.",
        },
        "gazon_fito": {
            "name": "Fito gazon (kg)",
            "photo": "AgACAgIAAxkBAAIDZ2rR9wzgxpH9Bv9J9upi13XYf9wBAAIQI2sbxW2RSo1TLRleJBaEAQADAgADeQADPQQ",
            "desc": "Fitopotensialga ega, chidamli va turli iqlim sharoitlariga tez moslashuvchi gazon.",
        },
    }

    current_gazon = gazon_info.get(call.data)
    if not current_gazon:
        return

    await state.update_data(
        stone_name=current_gazon["name"], price_text="100 000 so'm / kg"
    )

    caption = (
        f"🌱 **{current_gazon['name']}**\n\n"
        f"📖 **Ma'lumot:**\n{current_gazon['desc']}\n\n"
        f"💰 **Narxi:** 100 000 so'm / kg\n"
        f"ℹ️ *(10 kg va undan ko'p olsangiz — 95 000 so'mdan!)*\n\n"
        "Buyurtma berish uchun pastdagi tugmani bosing:"
    )

    await call.message.answer_photo(
        photo=current_gazon["photo"],
        caption=caption,
        reply_markup=order_gazon_inline_kb,
        parse_mode="Markdown",
    )


# === MANZARALI DARAXTLAR ===
@router.callback_query(F.data == "cat_trees")
async def list_trees(call: CallbackQuery):
    text = "🌲 **Manzarali daraxtlar va butalar katalogi**\n\nKerakli o'simlikni tanlang:"
    try:
        await call.message.delete()
    except Exception:
        pass

    await call.message.answer(
        text, reply_markup=tree_items_kb, parse_mode="Markdown"
    )
    await call.answer()


@router.callback_query(F.data == "back_to_trees")
async def back_to_trees_handler(call: CallbackQuery):
    text = "🌲 **Manzarali daraxtlar va butalar katalogi**\n\nKerakli o'simlikni tanlang:"
    
    try:
        await call.message.delete()
    except Exception:
        pass

    await call.message.answer(text, reply_markup=tree_items_kb, parse_mode="Markdown")
    await call.answer()


@router.callback_query(
    F.data.in_(
        [
            "tree_ligustrum_pyramid",
            "tree_euonymus_pyramid",
            "tree_photinia_pyramid",
            "tree_euonymus_stamba",
            "tree_arizonica",
            "tree_photinia_globe",
            "tree_rose_italy",
        ]
    )
)
async def show_tree_details(call: CallbackQuery, state: FSMContext):
    # 1. Eski ro'yxat xabarini o'chirib yuboramiz
    try:
        await call.message.delete()
    except Exception:
        pass
    await call.answer()

    trees_data = {
        "tree_ligustrum_pyramid": {
            "name": "Ligustrum piramida",
            "price": "2.350.000 so'm",
            "photo": "AgACAgIAAxkBAAIH1GrTONgX7A8-UdFSa84uUXW6fG1JAAKqH2sbxW2ZSmrYPWMCddXiAQADAgADeAADPQQ",
            "desc": (
                "🌿 **Ligustrum piramida** *(Ligustrum lucidum 'Pyramid')*\n\n"
                "📖 **Ma'lumot:**\n"
                "🚰 Sug'orish: O'rtacha, tuproq quriganda sug'oriladi.\n"
                "🌤 Quyosh: Quyoshli yoki yarim soya joy va unumdor tuproq.\n"
                "❄️ Sovuqqa chidamliligi: Yaxshi, qishki sovuqlarga bardoshli.\n"
                "🪏 Parvarish: Piramida shaklini saqlash uchun vaqti-vaqti bilan qirqiladi.\n"
                "💵 Narxi: 2.350.000 so'm\n\n"
                "Buyurtma berish uchun pastdagi tugmani bosing:"
            ),
        },
        "tree_euonymus_pyramid": {
            "name": "Ionomus piramida",
            "price": "1.100.000 so'm",
            "photo": "AgACAgIAAxkBAAIH5GrTOetGxHifuSjuFkRCUsIhYqWTAAKuH2sbxW2ZSr9yafpw9wxrAQADAgADeAADPQQ",
            "desc": (
                "🌿 **Ionomus piramida** *(Euonymus japonicus 'Pyramid')*\n\n"
                "📖 **Ma'lumot:**\n"
                "🚰 Sug'orish: Botqoqni yoqtirmaydi, tuproq quriganda mo'tadil sug'oriladi.\n"
                "🌤 Quyosh: Yorqin rangini saqlashi uchun quyoshli yoki yarim soya joy.\n"
                "❄️ Sovuqqa chidamliligi: O'rtacha; keskin sovuqda muzlab, bahorda tiklanadi.\n"
                "🪏 Parvarish: Piramida shaklini saqlash uchun qirqib turiladi.\n"
                "💵 Narxi: 1.100.000 so'm\n\n"
                "Buyurtma berish uchun pastdagi tugmani bosing:"
            ),
        },
        "tree_photinia_pyramid": {
            "name": "Fatiniya piramida",
            "price": "2.350.000 so'm",
            "photo": "AgACAgIAAxkBAAIHy2rTOGhLvgvtfv0SHBOGAAHWJnr7QQACpx9rG8VtmUp1ikT1RjvungEAAwIAA3gAAz0E",
            "desc": (
                "🌿 **Fatiniya piramida** *(Photinia x fraseri 'Pyramid')*\n\n"
                "📖 **Ma'lumot:**\n"
                "🚰 Sug'orish: O'rtacha, tuproq qurishiga qarab sug'oriladi.\n"
                "🌤 Quyosh: Qizil barglari yorqin bo'lishi uchun quyoshli joy lozim.\n"
                "❄️ Sovuqqa chidamliligi: O'rtacha; qattiq qishda biroz himoya talab qiladi.\n"
                "🪏 Parvarish: Yangi qizil novdalar va shaklni saqlash uchun qirqiladi.\n"
                "💵 Narxi: 2.350.000 so'm\n\n"
                "Buyurtma berish uchun pastdagi tugmani bosing:"
            ),
        },
        "tree_euonymus_stamba": {
            "name": "Ionomus shtamp katta",
            "price": "2.800.000 so'm",
            "photo": "AgACAgIAAxkBAAIHxWrTOC2mHZaxo8Way5VYF1y2aC9XAAKmH2sbxW2ZShseICvJtI05AQADAgADeAADPQQ",
            "desc": (
                "🌿 **Ionomus shtamp katta** *(Euonymus japonicus 'Stamba')*\n\n"
                "📖 **Ma'lumot:**\n"
                "🚰 Sug'orish: Ortiqcha suvni yoqtirmaydi, o'rtacha sug'oriladi.\n"
                "🌤 Quyosh: Quyoshli yoki yarim soya joyga ekiladi.\n"
                "❄️ Sovuqqa chidamliligi: O'rtacha; keskin qahratonda bahorda qayta tiklanadi.\n"
                "🪏 Parvarish: Daraxtsimon (shtamp) toji qirqib shakllantiriladi.\n"
                "💵 Narxi: 2.800.000 so'm\n\n"
                "Buyurtma berish uchun pastdagi tugmani bosing:"
            ),
        },
        "tree_arizonica": {
            "name": "Arizonika Kiparis primoy",
            "price": "800.000 so'm",
            "photo": "AgACAgIAAxkBAAIHwmrTOBaTTATtWw8DkcC15ZDVLDp6AAKlH2sbxW2ZSt0i73wLw5XhAQADAgADeAADPQQ",
            "desc": (
                "🌿 **Arizonika Kiparis primoy** *(Cupressus arizonica 'Fastigiata')*\n\n"
                "📖 **Ma'lumot:**\n"
                "🚰 Sug'orish: O'rtacha; o'rnashgach qurg'oqchilikka juda chidamli.\n"
                "🌤 Quyosh: Ochiq quyoshli joy va drenajli tuproq.\n"
                "❄️ Sovuqqa chidamliligi: Yuqori, qahraton sovuqqa bardoshli.\n"
                "🪏 Parvarish: Tik va ixcham o'sadi, deyarli qirqish talab qilmaydi.\n"
                "💵 Narxi: 800.000 so'm\n\n"
                "Buyurtma berish uchun pastdagi tugmani bosing:"
            ),
        },
        "tree_photinia_globe": {
            "name": "Fatiniya shar",
            "price": "2.050.000 so'm",
            "photo": "AgACAgIAAxkBAAIH12rTOPf2NIjEJcTieRhb6_5SvPMLAAKrH2sbxW2ZSpT4THI8lZlOAQADAgADeAADPQQ",
            "desc": (
                "🌿 **Fatiniya shar** *(Photinia x fraseri 'Globosa')*\n\n"
                "📖 **Ma'lumot:**\n"
                "🚰 Sug'orish: Tuproq quriganda mo'tadil sug'oriladi.\n"
                "🌤 Quyosh: Qizil yorqin barglari uchun quyoshli joy ma'qul.\n"
                "❄️ Sovuqqa chidamliligi: O'rtacha yaxshi.\n"
                "🪏 Parvarish: Sharsimon shaklini saqlash uchun qirqib turiladi.\n"
                "💵 Narxi: 2.050.000 so'm\n\n"
                "Buyurtma berish uchun pastdagi tugmani bosing:"
            ),
        },
        "tree_rose_italy": {
            "name": "Roza shtamp italy",
            "price": "950.000 so'm",
            "photo": "AgACAgIAAxkBAAIH2mrTOQejJ_YvKmNUwhZuZ0m1yX8qAAKsH2sbxW2ZSgS_ZDPGo7LaAQADAgADeAADPQQ",
            "desc": (
                "🌿 **Roza shtamp italy** *(Rosa Stamba - Chetdan keltirilgan)*\n\n"
                "📖 **Ma'lumot:**\n"
                "🚰 Sug'orish: Muntazam, ildizidan mo'tadil sug'oriladi.\n"
                "🌤 Quyosh: Quyoshli joy va unumdor tuproq talab etadi.\n"
                "❄️ Sovuqqa chidamliligi: Qishda tanasi va ustini sovuqdan o'rash tavsiya etiladi.\n"
                "🪏 Parvarish: Gullab bo'lgach qirqish va o'g'itlash kerak.\n"
                "💵 Narxi: 950.000 so'm\n\n"
                "Buyurtma berish uchun pastdagi tugmani bosing:"
            ),
        },
    }

    tree = trees_data.get(call.data)
    if not tree:
        return

    await state.update_data(stone_name=tree["name"], price_text=tree["price"])

    # Buyurtma berish tugmasi
    only_order_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🛒 Buyurtma berish", callback_data="order_stone")]
        ]
    )

    # 2. Tanlangan daraxtning rasmi va ma'lumotini yuboramiz (Buyurtma tugmasi bilan)
    await call.message.answer_photo(
        photo=tree["photo"],
        caption=tree["desc"],
        reply_markup=only_order_kb,
        parse_mode="Markdown",
    )

    # 3. Ostidan darhol daraxtlar ro'yxatini chiqaramiz
    await call.message.answer(
        "🌲 **Manzarali daraxtlar va butalar katalogi**\n\nKerakli o'simlikni tanlang:",
        reply_markup=tree_items_kb,
        parse_mode="Markdown",
    )

# === DEKORATIV TOSHLAR ===
@router.callback_query(F.data == "cat_stones")
async def stone_section_callback(call: CallbackQuery):
    try:
        await call.message.delete()
    except Exception:
        pass
    video_id = "BAACAgQAAxkBAAIFQmrSaZ1lds4gE6Hnda54L6qsvwfiAAL2CwAC-S80UkY-ovPDvisTPQQ"
    await call.message.answer_video(video=video_id)
    text = "🪨 **Dekorativ toshlar bo'limiga xush kelibsiz!**\n\nKerakli tosh turini yoki rangini tanlang:"
    await call.message.answer(
        text, reply_markup=stone_main_kb, parse_mode="Markdown"
    )
    await call.answer()


@router.callback_query(F.data == "stone_decorations")
async def show_stone_decorations(call: CallbackQuery):
    try:
        await call.message.delete()
    except Exception:
        pass
    video_id = "BAACAgQAAxkBAAIFQmrSaZ1lds4gE6Hnda54L6qsvwfiAAL2CwAC-S80UkY-ovPDvisTPQQ"
    await call.message.answer_video(video=video_id)
    await call.answer()


@router.callback_query(
    F.data.in_(
        [
            "stone_Qizil",
            "stone_Oq",
            "stone_Kok",
            "stone_TomirchaQizil",
            "stone_Keramzit",
        ]
    )
)
async def select_stone_color(call: CallbackQuery, state: FSMContext):
    color_code = call.data.replace("stone_", "")
    names = {
        "Qizil": "Qizil tosh",
        "Oq": "Oq tosh",
        "Kok": "Ko'k tosh",
        "TomirchaQizil": "Tomircha Qizil tosh",
        "Keramzit": "Keramzit",
    }
    stone_name = names.get(color_code, color_code)
    await state.update_data(stone_name=stone_name, color_code=color_code)

    try:
        await call.message.delete()
    except Exception:
        pass

    if color_code == "Keramzit":
        await state.update_data(price_text="80 000 so'm / 1 qop")
        text = "🟠 **Keramzit**\n💰 **Narxi:** 80 000 so'm (1 qop)\n\nBuyurtma berish uchun pastdagi tugmani bosing:"
        await call.message.answer(
            text, reply_markup=order_inline_kb, parse_mode="Markdown"
        )
    else:
        text = f"🎨 **Tanlandi:** {stone_name}\n\nEndi kerakli o'lchamni tanlang:"
        await call.message.answer(
            text, reply_markup=stone_size_kb, parse_mode="Markdown"
        )
    await call.answer()


@router.callback_query(F.data.startswith("size_"))
async def select_stone_size(call: CallbackQuery, state: FSMContext):
    size_code = call.data.replace("size_", "")
    sizes = {
        "Kichkina": "Kichkina (Pista)",
        "Ortacha": "O'rtacha (Gugurt)",
        "Katta": "Katta (Tuxum)",
    }
    size_name = sizes.get(size_code, size_code)

    data = await state.get_data()
    color_code = data.get("color_code")
    prices = {
        "Qizil": "12 000 so'm / 1 kg",
        "Oq": "8 000 so'm / 1 kg",
        "Kok": "10 000 so'm / 1 kg",
        "TomirchaQizil": "10 000 so'm / 1 kg",
    }
    price_text = prices.get(color_code, "Kelishilgan holda")

    await state.update_data(size_name=size_name, price_text=price_text)

    try:
        await call.message.delete()
    except Exception:
        pass

    text = (
        f"🪨 **{data.get('stone_name')}**\n"
        f"📏 **O'lchami:** {size_name}\n"
        f"💰 **Narxi:** {price_text}\n\n"
        "Buyurtma berish uchun pastdagi tugmani bosing:"
    )
    await call.message.answer(
        text, reply_markup=order_inline_kb, parse_mode="Markdown"
    )
    await call.answer()


@router.callback_query(F.data == "stone_Xarsang")
async def xarsang_menu(call: CallbackQuery):
    try:
        await call.message.delete()
    except Exception:
        pass
    await call.message.answer(
        "🗿 **Katta xarsang toshlar turlari:**\nKeraklisini tanlang:",
        reply_markup=xarsang_kb,
        parse_mode="Markdown",
    )
    await call.answer()


@router.callback_query(F.data.in_(["buy_xarsang_kok", "buy_xarsang_oq"]))
async def select_xarsang(call: CallbackQuery, state: FSMContext):
    name = (
        "Katta ko'k tosh" if call.data == "buy_xarsang_kok" else "Katta oq tosh"
    )
    await state.update_data(
        stone_name=name, price_text="4 000 so'm / 1 kg", size_name="Xarsang"
    )
    try:
        await call.message.delete()
    except Exception:
        pass
    text = f"🗿 **{name}**\n💰 **Narxi:** 4 000 so'm / 1 kg\n\nBuyurtma berish uchun tugmani bosing:"
    await call.message.answer(
        text, reply_markup=order_inline_kb, parse_mode="Markdown"
    )
    await call.answer()


@router.callback_query(F.data == "stone_Yapaloq")
async def yapaloq_menu(call: CallbackQuery):
    try:
        await call.message.delete()
    except Exception:
        pass
    await call.message.answer(
        "🪨 **Katta yapaloq toshlar turlari:**\nKeraklisini tanlang:",
        reply_markup=yapaloq_kb,
        parse_mode="Markdown",
    )
    await call.answer()


@router.callback_query(F.data.in_(["buy_yapaloq_oq", "buy_yapaloq_kok"]))
async def select_yapaloq(call: CallbackQuery, state: FSMContext):
    name = (
        "Oq yapaloq tosh" if call.data == "buy_yapaloq_oq" else "Ko'k yapaloq tosh"
    )
    await state.update_data(
        stone_name=name, price_text="4 000 so'm / 1 kg", size_name="Yapaloq"
    )
    try:
        await call.message.delete()
    except Exception:
        pass
    text = f"🪨 **{name}**\n💰 **Narxi:** 4 000 so'm / 1 kg\n\nBuyurtma berish uchun tugmani bosing:"
    await call.message.answer(
        text, reply_markup=order_inline_kb, parse_mode="Markdown"
    )
    await call.answer()


@router.callback_query(F.data == "back_to_stones")
async def back_to_stones_handler(call: CallbackQuery):
    text = "🪨 **Dekorativ toshlar bo'limi:**\nKerakli tosh turini yoki rangini tanlang:"
    try:
        await call.message.delete()
    except Exception:
        pass

    await call.message.answer(
        text, reply_markup=stone_main_kb, parse_mode="Markdown"
    )
    await call.answer()


# === LOKATSIYA VA ALOQA ===
@router.callback_query(F.data == "cat_location")
async def send_location_callback(call: CallbackQuery):
    try:
        await call.message.delete()
    except Exception:
        pass

    await call.message.answer_location(
        latitude=LOCATION_LAT, longitude=LOCATION_LON
    )
    
    await call.message.answer(
        LOCATION_TEXT, 
        parse_mode="Markdown"
    )
    
    await call.message.answer(
        "Quyidagi bo'limlardan birini tanlang:",
        reply_markup=main_menu_kb,
        parse_mode="Markdown"
    )
    await call.answer()


@router.callback_query(F.data == "cat_contact")
async def contact_us_callback(call: CallbackQuery):
    text = (
        "📞 **Biz bilan bog'lanish uchun ma'lumotlar:**\n\n"
        "📱 **Telefon raqamlar:**\n"
        "+998-93-722-41-11\n"
        "+998-94-994-00-07\n\n"
        "💬 **Telegram usernames:**\n"
        "@ydbekzod | @Baxodir4111\n\n"
        "📸 **Instagram:**\n"
        "https://www.instagram.com/landshaft.dizayn.sam\n\n"
        "🌐 **Taplink:**\n"
        "https://taplink.cc/landshaftdizaynsam\n\n"
        "📍 **Manzilimizni yuqoridagi 'Ko'chatxonamiz Joylashuvi' tugmasi orqali ko'rishingiz mumkin.**"
    )
    
    try:
        await call.message.delete()
    except Exception:
        pass

    await call.message.answer(
        text, 
        parse_mode="Markdown"
    )
    
    await call.message.answer(
        "Quyidagi bo'limlardan birini tanlang:",
        reply_markup=main_menu_kb,
        parse_mode="Markdown"
    )
    await call.answer()


# === BUYURTMA QILISH VA TELEFON RAQAM QABUL QILISH ===
@router.callback_query(F.data == "order_stone")
async def order_stone_handler(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
    except Exception:
        pass
        
    await call.message.answer(
        "📱 Buyurtmani rasmiylashtirish uchun telefon raqamingizni yuboring: (Pastdagi tugmani bosing)",
        reply_markup=phone_req_kb,
    )
    await state.set_state(Form.waiting_for_phone)
    await call.answer()


@router.message(Form.waiting_for_phone, F.contact)
async def process_phone(message: Message, state: FSMContext):
    data = await state.get_data()
    phone = message.contact.phone_number
    user = message.from_user

    item_name = (
        data.get("stone_name") or data.get("service_name") or "Ko'rsatilmagan"
    )

    amount_info = (
        data.get("m2") and f"{data.get('m2')} m²"
        or data.get("size_name")
        or "Ko'rsatilmagan"
    )

    total_price = data.get("total") or data.get("price_text") or "Kiritilmagan"

    details = (
        f"🛠 **Mahsulot/Xizmat:** {item_name}\n"
        f"📐 **O'lchami / Miqdori:** {amount_info}\n"
        f"💰 **Narxi / Summasi:** {total_price}"
    )

    await send_to_group(message.bot, user, details, phone=phone)

    # Pastdagi reply tugmalarni tozalaymiz
    try:
        remove_msg = await message.answer("...", reply_markup=ReplyKeyboardRemove())
        await remove_msg.delete()
    except Exception:
        pass

    await message.answer(
        "✅ **Buyurtmangiz muvaffaqiyatli qabul qilindi!**\n\n"
        "Tez orada operatorlarimiz siz bilan bog'lanishadi.",
        reply_markup=main_menu_kb,
        parse_mode="Markdown",
    )

    await state.clear()