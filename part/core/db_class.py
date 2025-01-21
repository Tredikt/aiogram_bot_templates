from sqlalchemy.orm import Session

from user.repositories.user import UserRepository


class DBClass:
    def __init__(self, session: Session):
        self.user = UserRepository(session=session)
    