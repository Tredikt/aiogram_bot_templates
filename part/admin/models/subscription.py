from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db_templates import BaseModel


class Subscription(BaseModel):
    __tablename__ = "subscription"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    price: Mapped[int] = mapped_column(unique=True)
    duration: Mapped[int] = mapped_column(unique=True, nullable=False)

    customer: Mapped["Customer"] = relationship(argument="Customer", back_populates="subscription")