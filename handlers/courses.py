from aiogram import Router, F, types
from aiogram.filters import Command

from keyboards.napravlenie import napravleniya_keyboard


courses_router = Router()

@courses_router.message(Command("courses"))
async def show_categories(message: types.Message):
    await message.answer("Выберите направление", reply_markup=napravleniya_keyboard())


@courses_router.message(F.text.lower() == "бекенд")
async def show_python_courses(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Курсы по Python", reply_markup=kb)

@courses_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f"Ваш контакт: {message.contact.phone_number}")

@courses_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f"Ваша геолокация: {message.location}")