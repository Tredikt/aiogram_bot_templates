from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

my_id_router = Router()


@my_id_router.message(Command(commands="my_id"))
async def my_id_handler(message: Message):
    user_id = message.from_user.id

    await message.answer(
        text=f"Ваш ID:\n<pre>{user_id}</pre>"
    )
