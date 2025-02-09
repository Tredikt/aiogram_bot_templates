from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from core.db_class import DBClass

configure_router = Router()


@configure_router.message(Command("configure"))
async def configure(message: Message, db: DBClass):
    pass