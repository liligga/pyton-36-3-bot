import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from aiogram.filters import Command
import logging


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()



@dp.message(Command("pic"))
async def send_pic(message: types.Message):
    file = types.FSInputFile("images/cat.jpg")
    await message.answer_photo(
        photo=file,
        caption="Котик"
    )

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}")

@dp.message()
async def echo(message: types.Message):
    # обрабатываем все сообщения
    # await message.answer(f"{message.text}, {message.from_user.first_name}, {message.from_user.username}")
    await message.reply(
        f"{message.text}, {message.from_user.first_name}, {message.from_user.username}"
    )


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="pic", description="Получить картинку")
    ])

    # запускаем бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())