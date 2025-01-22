from aiogram.fsm.state import State, StatesGroup


class AdminStates(StatesGroup):
    mailing = State()
    rights = State()

    add_admin = State()
    add_subscription = State()

