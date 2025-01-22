from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from core.db_templates import BaseModel


class Admin(BaseModel):
    __tablename__ = "admin"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"))

    can_edit_admin: Mapped[bool] = mapped_column(default=False)
    can_edit_subscription: Mapped[bool] = mapped_column(default=True)

    user: Mapped["User"] = relationship(
        argument="User",
        back_populates="admin",
    )
