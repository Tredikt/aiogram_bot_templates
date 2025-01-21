from sqlalchemy import select, insert, update

from user.models.user import User
from core.db_templates import BaseRepository


class UserRepository(BaseRepository):

    def add_user(
            self,
            user_id: int,
            first_name: str,
            full_name: str,
            last_name: str | None = None,
            username: str | None = None,
    ):
        insert_stmt = insert(User).values(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            username=username,
        )

        self.session.execute(statement=insert_stmt)
        self.session.commit()

    def get_user(
            self,
            user_id: int | None = None,
            many: bool | None = None,
    ):
        if user_id:
            select_stmt = select(User).where(User.user_id == user_id)

            result = self.session.execute(statement=select_stmt)
            return result.scalar_one_or_none()

        elif many:
            select_query = select(User.user_id)
            result = self.session.execute(statement=select_query)
            return result.scalars().all()

        else:
            return None

    def update_user(
            self,
            user_id: int,
            **kwargs
    ):
        update_stmt = update(User).where(User.user_id == user_id).values(**kwargs)

        self.session.execute(statement=update_stmt)
        self.session.commit()
