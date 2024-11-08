from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards import Keyboards
from settings import env_settings

admin_router = Router()


@admin_router.callback_query(F.data == "admin")
@admin_router.message(Command(commands=["admin"]))
async def admin_handler(update: Message | CallbackQuery, state: FSMContext, keyboards: Keyboards):
    await state.clear()
    user_id = str(update.from_user.id)

    if user_id in env_settings.split(","):
        text = "Админка:"
        keyboard = await keyboards.admin.admin_menu()

        if update.__class__.__name__ == "CallbackQuery":
            await update.message.edit_text(
                text=text,
                reply_markup=keyboard
            )

        else:
            await update.answer(
                text=text,
                reply_markup=keyboard
            )

