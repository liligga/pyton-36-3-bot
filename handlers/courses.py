from aiogram import Router, F, types
from aiogram.filters import Command

from keyboards.napravlenie import napravleniya_keyboard
from db.queries import get_courses, get_teachers_by_course_id, get_teachers_by_course_name

courses_router = Router()

def free_lesson_singup(course_id: int):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Записаться на бесплатный урок", callback_data=f'free_lesson:{course_id}'),
                types.InlineKeyboardButton(text="Информация", callback_data=f"course_info:{course_id}"),
            ]
        ]
    )
    return kb

@courses_router.message(Command("courses"))
async def show_categories(message: types.Message):
    courses = get_courses()
    await message.answer("Выберите направление")
    #  reply_markup=napravleniya_keyboard())
    for course in courses:
        await message.answer(course[1], reply_markup=free_lesson_singup(course[0]))



@courses_router.message(F.text.lower() == "бекенд")
async def show_python_courses(message: types.Message):
    # teachers = get_teachers_by_course_id(2)
    teachers = get_teachers_by_course_name("Backend")
    kb = types.ReplyKeyboardRemove()
    
    await message.answer("Курсы по Python. Наши преподаватели:", reply_markup=kb)
    for teacher in teachers:
        await message.answer("Имя: " + teacher[1])

@courses_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f"Ваш контакт: {message.contact.phone_number}")

@courses_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f"Ваша геолокация: {message.location}")