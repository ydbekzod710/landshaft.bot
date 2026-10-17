from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from config import ADMIN_IDS

router = Router()


@router.message(Command("admin"))
async def admin_panel(message: Message):
  if message.from_user.id not in ADMIN_IDS:
    return
  await message.answer(
      "👨‍💻 Admin panelga xush kelibsiz!\n\nXabarnoma yuborish uchun:"
      " `/rassilka Matn` ko'rinishida yozing."
  )


@router.message(Command("rassilka"))
async def broadcast(message: Message):
  if message.from_user.id not in ADMIN_IDS:
    return
  text = message.text.replace("/rassilka", "").strip()
  if not text:
    await message.answer("Iltimos, tarqatiladigan xabar matnini ham yozing.")
    return

  await message.answer(f"✅ Xabarnoma yuborish boshlandi:\n\n{text}")


# Videoni yuborganda xatosiz file_id chiqarish (Markdown'siz)
@router.message(F.video)
async def get_video_id(message: Message):
  if message.from_user.id in ADMIN_IDS:
    file_id = message.video.file_id
    await message.answer(f"Videongizning file_id kodi:\n\n{file_id}")



  # Rasm yoki video yuborilganda xatosiz file_id chiqarish
@router.message(F.photo | F.video)
async def get_media_id(message: Message):
    if message.from_user.id in ADMIN_IDS:
        if message.video:
            file_id = message.video.file_id
            media_type = "Video"
        elif message.photo:
            # Rasmlar bir nechta hajmda keladi, eng oxirgisi eng yuqori sifatlisi hisoblanadi
            file_id = message.photo[-1].file_id
            media_type = "Rasm"
        else:
            return
        
        await message.answer(f"{media_type} ning file_id kodi:\n\n{file_id}")