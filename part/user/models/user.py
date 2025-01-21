from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from core.db_templates import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=True)
    full_name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=True)
