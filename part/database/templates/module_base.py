from sqlalchemy.ext.asyncio import AsyncSession


class ModuleBase:
    def __init__(self, session):
        self.session: AsyncSession = session
