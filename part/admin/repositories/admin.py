from sqlalchemy import insert, select, update, delete

from core.db_templates.base_repository import BaseRepository
from admin.models.admin import Admin


class AdminRepository(BaseRepository):

    def add(self, user_id: int):
        insert_stmt = insert(Admin).values(user_id=user_id).returning(Admin)

        result = self.session.execute(statement=insert_stmt).scalar_one()
        self.session.commit()

        return result

    def get(
        self,
        user_id: int | None = None,
        every: bool | None = None
    ) -> Admin | list[Admin] | None:
        result = None

        if user_id:
            select_stmt = select(Admin).where(
                Admin.user_id == user_id
            )
            result = self.session.execute(statement=select_stmt).scalar_one_or_none()

        elif every:
            select_stmt = select(Admin)
            result = self.session.execute(statement=select_stmt).scalars().all()

        return result

    def update(
        self,
        user_id: int,
        **kwargs
    ) -> Admin:
        print("КВАРГИ", kwargs)
        update_stmt = update(Admin).where(
            Admin.user_id == user_id
        ).values(**kwargs).returning(Admin)

        result = self.session.execute(statement=update_stmt).scalar_one()
        self.session.commit()

        return result

    def delete(self, user_id: int):
        delete_stmt = delete(Admin).where(
            Admin.user_id == user_id
        )

        self.session.execute(statement=delete_stmt)
        self.session.commit()

