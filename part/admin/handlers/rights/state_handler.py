from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from admin.fsm_machine.admin import AdminStates
from core.db_class import DBClass
from core.keyboards import Keyboards

rights_state_router = Router()


@rights_state_router.message(F.text, StateFilter(AdminStates.add_admin))
async def add_admin_state_handler(message: Message, state: FSMContext, db: DBClass, keyboards: Keyboards):
    admin_id = message.text

    if admin_id.isdigit():
        admin = db.admin.add(user_id=int(admin_id))
        keyboard = await keyboards.admin.rights.admin_rights(admin=admin)

        await message.answer(
            text=f"<i>Админ успешно добавлен.\nИнформация об админе: <b>{admin.user.full_name}</b></i>",
            reply_markup=keyboard
        )

        await state.clear()

    else:
        keyboard = await keyboards.admin.rights.to_rights()
        await message.answer(
            text="<i>Telegram ID должно быть числом. Повторите попытку или вернитесь в админ-панель</i>",
            reply_markup=keyboard
        )
