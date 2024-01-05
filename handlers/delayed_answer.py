from aiogram import Router, F, types
from aiogram.filters import Command
from bot import bot, scheduler
from datetime import datetime


delayed_answer_router = Router()

# "напомни сделать ДЗ по программированию"
# celery
@delayed_answer_router.message(F.text.startswith("напомни"))
async def reminder(message: types.Message):
    id=str(message.from_user.id)
    if scheduler.get_job(id) is not None:
        # await message.answer("Вы уже установили напоминание")
        # return
        scheduler.remove_job(id)
    await message.answer("Напоминание будет срабатывать каждые 20 секунд")
    # scheduler.add_job(
    #     send_reminder,
    #     id=id,
    #     trigger="interval", # interval, date, cron
    #     seconds=20,
    #     kwargs={"chat_id": message.from_user.id}
    # )
    # scheduler.add_job(
    #     send_reminder,
    #     id=id,
    #     trigger="date",
    #     run_date=datetime(2023, 12, 29, 16, 52, 20),
    #     kwargs={"chat_id": message.from_user.id}
    # )
    scheduler.add_job(
        send_reminder,
        id=id,
        trigger="cron",
        day_of_week="mon-fri",
        hour=17,
        minute=2,
        kwargs={"chat_id": message.from_user.id}
    )


async def send_reminder(chat_id: int):
    await bot.send_message(
        chat_id=chat_id,
        text="сделать ДЗ по программированию"
    )