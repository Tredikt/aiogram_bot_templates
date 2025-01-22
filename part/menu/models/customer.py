from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db_templates import BaseModel


class Customer(BaseModel):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"))
    subscription_id: Mapped[int] = mapped_column(ForeignKey("subscription.id"))

    user: Mapped["User"] = relationship(
        argument="User",
        back_populates="customer",
    )

    subscription: Mapped["Subscription"] = relationship(
        argument="Subscription",
        back_populates="customer",
    )
