from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards import Keyboards

start_router = Router()


@start_router.message(Command(commands=["start"]))
async def start_handler(message: Message, state: FSMContext, keyboards: Keyboards):
    await state.clear()

    keyboard = await keyboards.menu.menu()
    await message.answer(
        text="Добро пожаловать!",
        reply_markup=keyboard
    )
