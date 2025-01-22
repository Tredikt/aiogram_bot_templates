from sqlalchemy import insert, select, update, delete

from core.db_templates.base_repository import BaseRepository
from admin.models.subscription import Subscription


class SubscriptionRepository(BaseRepository):

    def add(
        self,
        title: str,
        price: int,
        duration: int
    ) -> None:
        insert_stmt = insert(Subscription).values(
            title=title,
            price=price,
            duration=duration
        )

        self.session.execute(statement=insert_stmt)
        self.session.commit()

    def get(
        self,
        subscription_id: int | None = None,
        every: bool = False
    ) -> Subscription | list[Subscription] | None:
        result = None

        if subscription_id:
            select_stmt = select(Subscription).where(
                Subscription.id == subscription_id
            )

            result = self.session.execute(statement=select_stmt).scalar_one_or_none()

        elif every:
            select_stmt = select(Subscription).order_by(Subscription.price.asc())
            result = self.session.execute(statement=select_stmt).scalars().all()

        return result

    def update(self, subscription_id: int, **kwargs) -> None:
        update_stmt = update(Subscription).where(
            Subscription.id == subscription_id
        ).values(**kwargs)

        self.session.execute(statement=update_stmt)
        self.session.commit()

    def delete(self, subscription_id: int) -> None:
        delete_stmt = delete(Subscription).where(
            Subscription.id == subscription_id
        )

        self.session.execute(statement=delete_stmt)
        self.session.commit()
