from aiogram import Router, F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from admin.fsm_machine.admin import AdminStates
from core.db_class import DBClass
from core.keyboards import Keyboards

subscription_state_router = Router()


@subscription_state_router.message(F.text, StateFilter(AdminStates.add_subscription))
async def subscription_addition_state_handler(message: Message, state: FSMContext, bot: Bot, db: DBClass, keyboards: Keyboards):
    state_data = await state.get_data()
    data = message.text

    mode = state_data.get("mode", "title")
    messages_list = state_data.get("messages_list", list())
    sent_message = None

    keyboard = await keyboards.admin.subscriptions.to_menu()

    if mode == "title":
        sent_message = await message.answer(
            text="<i>Теперь введите длительность подписки (в днях)</i>",
            reply_markup=keyboard
        )
        await state.update_data(title=data, mode="duration")

    elif mode == "duration":
        if not data.isdigit():
            await message.answer(
                text="<i>Длительность должна быть цифрой, если вы хотите сделать её месячной, введите 30</i>",
                reply_markup=keyboard
            )

        else:
            sent_message = await message.answer(
                text="<i>Введите цену подписки (целым числом):</i>",
                reply_markup=keyboard
            )
            await state.update_data(duration=data, mode="price")

    elif mode == "price":
        if not data.isdigit():
            await message.answer(
                text="<i>Цена должна быть цифрой, например 999</i>",
                reply_markup=keyboard
            )

        else:
            title = state_data["title"]
            duration = state_data["duration"]
            price = data

            db.subscription.add(title=title, duration=duration, price=price)

            user_id = message.from_user.id

            messages_list.append(message.message_id)
            for message_id in messages_list:
                await bot.delete_message(chat_id=user_id, message_id=message_id)

            keyboard = await keyboards.admin.to_menu()
            await message.answer(
                text='<i>Запись "Подписки" успешно добавлена</i>',
                reply_markup=keyboard
            )

            await state.clear()
            return

    messages_list.append(message.message_id)
    if sent_message:
        messages_list.append(sent_message.message_id)
