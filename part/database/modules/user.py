from typing import Optional

from sqlalchemy import select, insert

from ..models import User
from ..templates import ModuleBase


class UserModule(ModuleBase):
    async def add_user(
            self,
            uuid: int,
            full_name: str,
            username: str
    ):
        insert_query = insert(User).values(
            uuid=uuid,
            full_name=full_name,
            username=username
        )

        await self.session.execute(statement=insert_query)
        await self.session.commit()

    async def get_user(
            self,
            uuid: Optional[int],
            many: Optional[bool]
    ):
        if uuid:
            select_query = select(User).where(
                uuid=uuid
            )

        else:
            select_query = select(User.uuid)

        await self.session.execute(statement=select_query)
        await self.session.commit()


