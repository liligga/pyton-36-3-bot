from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from pprint import pprint

from keyboards.napravlenie import napravleniya_keyboard
from db.queries import save_free_lesson_participant


# FSM = Finite state machine
# Конечный автомат
free_lesson_form_router = Router()

class Form(StatesGroup):
    name = State()
    age = State()
    napravlenie = State()
    phone = State()


# @free_lesson_form_router.message(Command("free_lesson"))
# async def start(message: types.Message, state: FSMContext):
#     await state.set_state(Form.name)
#     await message.answer("Как Вас зовут?")

@free_lesson_form_router.callback_query(F.data.startswith("free_lesson:"))
async def free_lesson(callback: types.CallbackQuery, state: FSMContext):
    # "free_lesson:1"
    course_id = int(callback.data.split(":")[1])
    # await callback.message.answer("Спасибо. ID курса " + str(course_id))
    await state.set_state(Form.name)
    await callback.message.answer("Как Вас зовут?")

@free_lesson_form_router.message(Command("stop"))
@free_lesson_form_router.message(F.text == "stop")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Ок")


@free_lesson_form_router.message(Form.name)
async def process_name(message: types.Message, state: FSMContext):
    if len(message.text) < 3:
        await message.answer("Слишком короткое имя")
        # return
    else:
        await state.update_data(name=message.text)
        await message.answer(f"Спасибо, {message.text}")

        await state.set_state(Form.age)
        await message.answer("Сколько Вам лет?")


@free_lesson_form_router.message(Form.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Пожалуйста вводите только цифры")
    elif int(age)<13 or int(age)>80:
        await message.answer("Пожалуйста вводите правильный возраст")
    else:
        await state.update_data(age=int(age))
        await state.set_state(Form.napravlenie)
        await message.answer("По какому направлению вы хотите учиться?", reply_markup=napravleniya_keyboard())


@free_lesson_form_router.message(Form.napravlenie)
async def process_napravlenie(message: types.Message, state: FSMContext):
    await state.update_data(napravlenie=message.text)

    kb = types.ReplyKeyboardRemove()
    await state.set_state(Form.phone)
    await message.answer("Ваш номер телефона?", reply_markup=kb)


@free_lesson_form_router.message(Form.phone)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)

    data = await state.get_data()
    pprint(data)
    await message.answer(f"Спасибо!")
    save_free_lesson_participant(data, message.from_user.id)
    await state.clear()