from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards import Keyboards
from ..states_handlers import BotStates

admin_callback_router = Router()


@admin_callback_router.callback_query(F.data == "mailing_to_users")
async def mailing_callback_handler(call: CallbackQuery, state: FSMContext, keyboards: Keyboards):
    await state.set_state(BotStates.mailing)
    keyboard = await keyboards.admin.to_menu()

    await call.message.edit_text(
        text="Введите сообщения для рассылки пользователям:",
        reply_markup=keyboard
    )