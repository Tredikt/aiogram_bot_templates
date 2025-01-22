from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from admin.fsm_machine.admin import AdminStates
from core.db_class import DBClass
from core.keyboards import Keyboards

subscriptions_callback_router = Router()


@subscriptions_callback_router.callback_query(F.data == "subscriptions")
async def subscriptions_callback_handler(call: CallbackQuery, keyboards: Keyboards):
    keyboard = await keyboards.admin.subscriptions.menu()

    await call.message.edit_text(
        text="<i>Управление подписками:</i>",
        reply_markup=keyboard
    )


@subscriptions_callback_router.callback_query(F.data == "add_subscription")
async def add_subscription_callback_handler(call: CallbackQuery, state: FSMContext, keyboards: Keyboards):
    await state.set_state(AdminStates.add_subscription)

    keyboard = await keyboards.admin.subscriptions.to_menu()

    sent_message = await call.message.edit_text(
        text='<i>Введите название подписки, оно будет видно на кнопке, например "7 дней"</i>:',
        reply_markup=keyboard
    )

    state_data = await state.get_data()
    messages_list = state_data.get("message_list", list())
    messages_list.append(sent_message.message_id)

    await state.update_data(mode="title", messages_list=messages_list)


@subscriptions_callback_router.callback_query(F.data == "subscriptions_list")
async def subscriptions_list_callback_handler(call: CallbackQuery, db: DBClass, keyboards: Keyboards):
    subscriptions = db.subscription.get(every=True)
    keyboard = await keyboards.admin.subscriptions.subscriptions_list(subscriptions=subscriptions)

    await call.message.edit_text(
        text="<i>Список подписок:</i>",
        reply_markup=keyboard
    )


@subscriptions_callback_router.callback_query(F.data.startswith("subscription_"))
async def subscription_callback_handler(call: CallbackQuery, db: DBClass, keyboards: Keyboards):
    subscription_id = int(call.data.split("_")[-1])
    subscription = db.subscription.get(subscription_id=subscription_id)
    keyboard = await keyboards.admin.subscriptions.to_menu()

    await call.message.edit_text(
        text=f"<i><b>Название: </b>{subscription.title}\n"
             f"<b>Длительность: </b>{subscription.duration}\n"
             f"<b>Цена: </b>{subscription.price}</i>",
        reply_markup=keyboard
    )

