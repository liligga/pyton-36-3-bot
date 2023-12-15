from aiogram import types

def napravleniya_keyboard():
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