from aiogram import types
from db.queries import get_courses

def napravleniya_keyboard():
    # courses = get_courses()
    # buttons = []
    # for course in courses:
    #     buttons.append(types.KeyboardButton(text=course[0]))

    kb = types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(text="Бекенд"),
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
    return kb