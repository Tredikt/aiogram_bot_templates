from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject
from sqlalchemy.orm import sessionmaker, Session

from core.db_class import DBClass
from core.keyboards import Keyboards


class BasicMiddleware(BaseMiddleware):
    def __init__(self, token: str, session: sessionmaker[Session]):
        self.token = token
        self.session = session

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]) -> Any:
        keyboards = Keyboards()
        data["keyboards"] = keyboards

        bot = Bot(token=self.token)
        data["bot"] = bot

        with self.session() as session:
            db = DBClass(session=session)
            data["db"] = db

        callback_query = event.callback_query
        message = event.message

        if callback_query:
            print(callback_query.data)

        elif message:
            user_id = message.from_user.id
            user = db.user.get(user_id=user_id)

            if not user:
                user_data = message.from_user

                db.user.add(
                    user_id=user_id,
                    first_name=user_data.first_name,
                    last_name=user_data.last_name,
                    full_name=user_data.full_name,
                    username=user_data.username
                )


        return await handler(event, data)
