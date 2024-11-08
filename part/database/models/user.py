from sqlalchemy import Column
from sqlalchemy import Integer, String

from ..templates import ModelBase


class User(ModelBase):
    __tablename__ = "user"

    uuid = Column(Integer, primary_key=True, unique=True, index=True)
    full_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
