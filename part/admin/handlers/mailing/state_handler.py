from aiogram import Router, F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from admin.fsm_machine.admin import AdminStates
from core.db_class import DBClass
from core.keyboards import Keyboards


mailing_state_router = Router()


@mailing_state_router.message(F.content_type.ANY, StateFilter(AdminStates.mailing))
async def mailing_state_handler(message: Message, state: FSMContext, bot: Bot, db: DBClass, keyboards: Keyboards):
    await state.clear()
    admin_id = message.from_user.id
    message_id = message.message_id

    users = db.user.get(every=True)

    for user in users:
        await bot.copy_message(
            chat_id=user,
            from_chat_id=admin_id,
            message_id=message_id
        )

    keyboard = await keyboards.admin.to_menu()
    await message.answer(
        text="<i>Рассылка успешно окончена</i>",
        reply_markup=keyboard
    )
