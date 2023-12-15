from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


# FSM = Finite state machine
# Конечный автомат
free_lesson_form_router = Router()

class Form(StatesGroup):
    name = State()
    age = State()
    napravlenie = State()
    phone = State()

@free_lesson_form_router.message(Command("free_lesson"))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("Как Вас зовут?")


@free_lesson_form_router.message(Form.name)
async def process_name(message: types.Message, state: FSMContext):
    await message.answer(f"Спасибо, {message.text}")
    await message.answer("Сколько Вам лет?")