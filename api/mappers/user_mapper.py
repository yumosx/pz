from pydantic import BaseModel, FiniteFloat
from sqlalchemy import Column, Text,Integer

from sqlmodel import Field

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from pydantic import BaseModel, Field


class User(BaseModel):
    __tablename__ = "users"

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    name: str = Field(sa_column=Column(Text, nullable=False))
    age: int = Field(sa_column=Column(Integer, nullable=False))
    phone: str = Field(sa_column=Column(String(15)))
    ctime: datetime = Field(
        sa_column=Column(DateTime, default=func.now(), nullable=False)
    )
    utime: datetime = Field(
        sa_column=Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    )
