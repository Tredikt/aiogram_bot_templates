import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from middlewares.basic_middleware import BasicMiddleware
from settings import env_settings

from database import ModelBase

from handlers import routers


async def main():
    logging.basicConfig(level=logging.INFO)

    telegram_token = env_settings.token
    # telegram_token = settings.test__telegram__token
    database_url = env_settings.database__url

    engine = create_async_engine(database_url)

    async with engine.begin() as conn:
        await conn.run_sync(ModelBase.metadata.create_all)

    session = async_sessionmaker(engine, expire_on_commit=False)

    storage = MemoryStorage()

    bot = Bot(token=telegram_token)
    dp = Dispatcher(bot=bot, storage=storage)

    dp.include_routers(*routers)

    dp.update.middleware(BasicMiddleware(token=env_settings.token, session=session))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def start_app():
    asyncio.run(main())


if __name__ == "__main__":
    start_app()
