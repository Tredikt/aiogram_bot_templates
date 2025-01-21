from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from core.db_templates import BaseModel
from user.models import User


class Admin(BaseModel):
    __tablename__ = "admin"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"))

    can_add_admin: Mapped[bool] = mapped_column(default=False)
    can_edit_price: Mapped[bool] = mapped_column(default=False)

    user: Mapped[User] = relationship(argument="User", back_populates="admin")
