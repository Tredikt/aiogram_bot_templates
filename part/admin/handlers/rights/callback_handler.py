from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from admin.fsm_machine.admin import AdminStates
from core.db_class import DBClass
from core.keyboards import Keyboards

rights_callback_router = Router()


@rights_callback_router.callback_query(F.data == "rights")
async def rights_callback_handler(call: CallbackQuery, state: FSMContext, keyboards: Keyboards):
    await state.clear()
    keyboard = await keyboards.admin.rights.admins()

    await call.message.edit_text(
        text="<i>Изменение прав админов:</i>",
        reply_markup=keyboard
    )


@rights_callback_router.callback_query(F.data == "add_admin")
async def add_admin_callback_handler(call: CallbackQuery, state: FSMContext, keyboards: Keyboards):
    await state.set_state(AdminStates.add_admin)
    keyboard = await keyboards.admin.rights.to_rights()

    await call.message.edit_text(
        text="<i>Введите Telegram ID пользователя, которого хотите добавить в админы, пользователь может получить ID по команде /my_id:</i>",
        reply_markup=keyboard
    )


@rights_callback_router.callback_query(F.data == "admins_list")
async def admins_list_callback_handler(call: CallbackQuery, db: DBClass, keyboards: Keyboards):
    admins = db.admin.get(every=True)
    keyboard = await keyboards.admin.rights.admins_list(admins=admins)

    await call.message.edit_text(
        text="<i>Список админов, здесь вы можете управлять их правами</i>:",
        reply_markup=keyboard
    )


@rights_callback_router.callback_query(F.data.startswith("admin_"))
async def admin_rights_callback_handler(call: CallbackQuery, db: DBClass, keyboards: Keyboards):
    admin_id = int(call.data.split("_")[-1])
    admin = db.admin.get(user_id=admin_id)
    keyboard = await keyboards.admin.rights.admin_rights(admin=admin)

    await call.message.edit_text(
        text=f"<i>Информация об админе: <b>{admin.user.full_name}</b></i>",
        reply_markup=keyboard
    )


@rights_callback_router.callback_query(F.data.startswith("can_"))
async def edit_admin_rights_callback_handler(call: CallbackQuery, db: DBClass, keyboards: Keyboards):
    call_data = call.data
    buttons = call.message.reply_markup.inline_keyboard
    is_true = "✅"

    for button in buttons:
        callback_data = button[0].callback_data
        if callback_data == call_data:
            text = button[0].text
            is_true = text.find("✅")

    call_data = call.data.split("_")
    admin_id = int(call_data[-1])
    parameter = "_".join(call_data[:-1])

    flag = False if is_true != -1 else True
    kwargs = {parameter: flag}

    admin = db.admin.update(user_id=admin_id, **kwargs)
    keyboard = await keyboards.admin.rights.admin_rights(admin=admin)

    await call.message.edit_reply_markup(reply_markup=keyboard)


@rights_callback_router.callback_query(F.data.startswith("delete_admin_"))
async def delete_admin_callback_handler(call: CallbackQuery, db: DBClass, keyboards: Keyboards):
    admin_id = int(call.data.split("_")[-1])
    db.admin.delete(user_id=admin_id)

    keyboard = await keyboards.admin.rights.to_rights()
    await call.message.edit_text(
        text="<i>Админ успешно удалён</i>",
        reply_markup=keyboard
    )
