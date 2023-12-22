from aiogram import Router, types
from aiogram.filters import Command


pic_router = Router()

@pic_router.message(Command("pic"))
async def send_pic(message: types.Message):
    msg = "Кот"
    picture_name = "cat.jpg"
    file = types.FSInputFile(f"images/{picture_name}")
    await message.answer_photo(
        photo=file,
        caption=msg
    )
