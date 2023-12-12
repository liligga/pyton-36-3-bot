from aiogram import Router, F, types
from aiogram.filters import Command


start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(url="https://geeks.kg/", text="Наш сайт"),
                types.InlineKeyboardButton(url="https://instagram.com/", text="Наш инстаграм"),
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about"),
            ]
        ]
    )
    await message.answer(
        f"""Привет, {message.from_user.full_name}. Мы компания Geeks, у нас вы можете стать настоящим програмистом.
        """, reply_markup=kb
    )
# handler = обработчик


@start_router.callback_query(F.data == "about")
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    
    await callback.message.answer("О нас")
