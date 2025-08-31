from sqlalchemy import Column
from sqlmodel import Field


class User:
    Id: int = Field(sa_column=Column(name="id"))