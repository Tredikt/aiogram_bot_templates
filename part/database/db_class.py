from sqlalchemy.ext.asyncio.session import AsyncSession

from modules import (
    UserModule,
)


class DBClass:
    def __init__(self, session: AsyncSession):
        self.user = UserModule(session=session)
