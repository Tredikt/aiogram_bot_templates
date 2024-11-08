from aiogram import Router, F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from database import DBClass
from keyboards import Keyboards
from .bot_states import BotStates

mailing_router = Router()


@mailing_router.message(F.content_type.ANY, StateFilter(BotStates.mailing))
async def mailing_state_handler(message: Message, state: FSMContext, bot: Bot, db: DBClass, keyboards: Keyboards):
    await state.clear()
    admin_id = message.from_user.id
    message_id = message.message_id

    users = await db.user.get_user(many=True)

    for user in users:
        await bot.copy_message(
            chat_id=user,
            from_chat_id=admin_id,
            message_id=message_id
        )

    keyboard = await keyboards.admin.back_to_admin()
    await message.answer(
        text="Рассылка успешно окончена",
        reply_markup=keyboard
    )
