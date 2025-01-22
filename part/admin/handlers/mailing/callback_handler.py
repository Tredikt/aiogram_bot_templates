from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from admin.fsm_machine.admin import AdminStates
from core.keyboards import Keyboards

mailing_callback_router = Router()


@mailing_callback_router.callback_query(F.data == "mailing")
async def mailing_callback_handler(call: CallbackQuery, state: FSMContext, keyboards: Keyboards):
    await state.set_state(AdminStates.mailing)
    keyboard = await keyboards.admin.to_menu()

    await call.message.edit_text(
        text="<i>Введите сообщения для рассылки пользователям:</i>",
        reply_markup=keyboard
    )
