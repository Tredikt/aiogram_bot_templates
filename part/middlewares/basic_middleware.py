from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject
from sqlalchemy.orm import sessionmaker, Session

from core.db_class import DBClass


class BasicMiddleware(BaseMiddleware):
    def __init__(self, token: str, session: sessionmaker[Session]):
        self.token = token
        self.session = session

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]) -> Any:

        if event.callback_query:
            print(event.callback_query.data)

        user_id = event.from_user.id

        bot = data.get("bot")
        db = data.get("db")

        if not bot:
            bot = Bot(token=self.token)
            data["bot"] = bot

        if not db:
            with self.session() as session:
                db = DBClass(session=session)

                data["db"] = db
                user = await db.user.get_user(user_id=user_id)
                if not user:
                    full_name = event.from_user.full_name
                    username = event.from_user.username

                    await db.user.add_user(
                        uuid=user_id,
                        full_name=full_name,
                        username=username
                    )

        return await handler(event, data)
