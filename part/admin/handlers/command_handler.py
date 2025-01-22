from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from admin.fsm_machine.admin import AdminStates
from core.bot_settings.commands import commands
from core.db_class import DBClass
from core.keyboards import Keyboards

from settings import env_settings


admin_command_router = Router()


@admin_command_router.callback_query(F.data == "admin")
@admin_command_router.message(Command(commands=["admin"]))
async def admin_command_handler(update: Message | CallbackQuery, state: FSMContext, bot: Bot, db: DBClass, keyboards: Keyboards):
    await state.clear()
    await bot.set_my_commands(commands=commands)

    user_id = update.from_user.id
    admin = db.admin.get(user_id=user_id)

    if admin or str(user_id) in env_settings.admins.split(","):
        rights = "all" if not admin else admin

        await state.set_state(AdminStates.rights)
        await state.update_data(rights=rights)

        text = "<i>Админ-панель:</i>"
        keyboard = await keyboards.admin.menu(rights=rights)

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

