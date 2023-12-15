from aiogram import Router, F, types
from aiogram.filters import Command


courses_router = Router()

@courses_router.message(Command("courses"))
async def show_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Python"),
                types.KeyboardButton(text="Тестирование"),
            ],
            [
                types.KeyboardButton(text="Фронтенд"),
            ],
            [
                types.KeyboardButton(text="Android"),
                types.KeyboardButton(text="iOS"),
            ],
            [
                types.KeyboardButton(text="Отправить мой номер", request_contact=True),
                types.KeyboardButton(text="Отправить мою геолокацию", request_location=True),
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите направление", reply_markup=kb)


@courses_router.message(F.text.lower() == "python")
async def show_python_courses(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Курсы по Python", reply_markup=kb)

@courses_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f"Ваш контакт: {message.contact.phone_number}")

@courses_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f"Ваша геолокация: {message.location}")