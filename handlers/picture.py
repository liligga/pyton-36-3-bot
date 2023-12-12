from aiogram import Router, types
from aiogram.filters import Command


pic_router = Router()

@pic_router.message(Command("pic"))
async def send_pic(message: types.Message):
    file = types.FSInputFile("images/cat.jpg")
    await message.answer_photo(
        photo=file,
        caption="Котик"
    )
