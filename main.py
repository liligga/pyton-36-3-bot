import asyncio
from aiogram import types
from aiogram.filters import Command
import logging
from bot import bot, dp
from handlers import (
    start_router,
    pic_router,
    courses_router,
    echo_router,
    free_lesson_form_router
)


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="pic", description="Получить картинку"),
        types.BotCommand(command="courses", description="Показать курсы"),
        types.BotCommand(command="free_lesson", description="Записаться на открытый урок"),
    ])
    
    dp.include_router(start_router)
    dp.include_router(pic_router)
    dp.include_router(courses_router)
    dp.include_router(free_lesson_form_router)

    # echo в самом конце
    dp.include_router(echo_router)
    # запускаем бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())