import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.db_templates import BaseModel
from middlewares.basic_middleware import BasicMiddleware
from settings import env_settings

from core.routers import routers


async def main():
    logging.basicConfig(level=logging.INFO)

    engine = create_engine(env_settings.database__url)

    BaseModel.metadata.create_all(bind=engine)
    session = sessionmaker(engine, expire_on_commit=False)

    storage = MemoryStorage()

    bot = Bot(token=env_settings.telegram__token, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher(bot=bot, storage=storage)

    dp.include_routers(*routers)

    dp.update.middleware(BasicMiddleware(token=env_settings.telegram__token, session=session))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def start_app():
    asyncio.run(main())


if __name__ == "__main__":
    start_app()
