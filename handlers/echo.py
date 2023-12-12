from aiogram import Router, F, types


echo_router = Router()

@echo_router.message(F.text)
async def echo(message: types.Message):
    # обрабатываем все сообщения
    # await message.answer(f"{message.text}, {message.from_user.first_name}, {message.from_user.username}")
    await message.reply(
        f"{message.text}, {message.from_user.first_name}, {message.from_user.username}"
    )