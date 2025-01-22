import asyncio
import aioschedule
from aiogram import Bot
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.db_class import DBClass
from settings import env_settings


bot = Bot(token=env_settings.telegram__token)

engine = create_engine(env_settings.database__url)
session = sessionmaker(engine, expire_on_commit=False)
with session() as session:
    db = DBClass(session=session)


async def subscription_checker():
    users = db.customer.get(expire_subscription=True)

    for user_id in users:
        await bot.send_message(
            chat_id=user_id,
            text="У вас закончилась подписка"
        )

        await db.customer.delete(user_id=user_id)


async def scheduler():
    aioschedule.every().day.at("10:00").do()

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(60)


async def main_schedule():
    await asyncio.create_task(scheduler())


if __name__ == '__main__':
    asyncio.run(main_schedule())