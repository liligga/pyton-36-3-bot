from aiogram import Router, F, types
from aiogram.filters import Command


group_admin_router = Router()
BAD_WORDS = ("дурак", "здрасть")


# @group_admin_router.message(F.from_user.id == 1428281770)
# @group_admin_router.message(F.from_user.id.in_({1428281770, 1111111}))
# @group_admin_router.message(F.message.photo)
# @group_admin_router.message(F.chat.type == "group")
@group_admin_router.message(F.chat.type.in_({"group", "supergroup"}))
@group_admin_router.message(Command("ban", prefix="!"))
async def ban(message: types.Message):
    await message.bot.ban_chat_member(
        chat_id=message.chat.id,
        user_id=message.from_user.id
    )


@group_admin_router.message(F.chat.type == "group")
async def catch_bad_words(message: types.Message):
    text = message.text.lower()
    for word in BAD_WORDS:
        if word in text:
            await message.reply("Вы используете запрещенные слова")
            await message.delete()
            break

