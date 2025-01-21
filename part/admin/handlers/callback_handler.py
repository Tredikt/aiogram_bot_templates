from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from admin.fsm_machine.admin import AdminStates
from admin.router import admin_router
from core.keyboards import Keyboards


@admin_router.callback_query(F.data == "mailing")
async def mailing_callback_handler(call: CallbackQuery, state: FSMContext, keyboards: Keyboards):
    await state.set_state(AdminStates.mailing)
    keyboard = await keyboards.admin.to_menu()

    await call.message.edit_text(
        text="Введите сообщения для рассылки пользователям:",
        reply_markup=keyboard
    )
