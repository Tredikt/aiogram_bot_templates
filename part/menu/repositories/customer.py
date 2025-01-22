from datetime import datetime, timedelta

from sqlalchemy import select, insert, delete, and_

from core.db_templates import BaseRepository

from menu.models.customer import Customer


class CustomerRepository(BaseRepository):

    def add(
        self,
        user_id: int,
        subscription_id: int
    ):
        insert_stmt = insert(Customer).values(
            user_id=user_id,
            subscription_id=subscription_id
        )

        self.session.execute(statement=insert_stmt)
        self.session.commit()

    def get(
        self,
        user_id: int | None = None,
        expire_subscription: bool | None = None
    ):
        result = None

        if expire_subscription:
            current_time = datetime.utcnow()
            select_stmt = select(Customer.user_id).where(
                and_(
                    Customer.created_at < current_time - (Customer.subscription.duration * timedelta(days=1))
                )
            )

            result = self.session.execute(statement=select_stmt).scalars().all()

        elif user_id:
            select_stmt = select(Customer).where(
                Customer.user_id == user_id
            )

            result = self.session.execute(statement=select_stmt).scalar_one_or_none()

        return result

    def delete(
        self,
        user_id: int | None = None,
        subscription_id: int | None = None
    ):
        delete_stmt = None

        if user_id:
            delete_stmt = delete(Customer).where(Customer.user_id == user_id)

        elif subscription_id:
            delete_stmt = delete(Customer).where(Customer.id == subscription_id)

        self.session.execute(statement=delete_stmt)
        self.session.commit()
