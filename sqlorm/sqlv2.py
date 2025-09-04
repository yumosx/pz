from sqlalchemy import Column, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Field, col

class UserMapper:
    Id: int = Field(sa_column=Column(name="id"))
    Name: str = Field(sa_column=Column(name="name"))

async def get_user(user_id: int, session: AsyncSession):
    condations = [
        col(UserMapper.Id) == user_id,
    ]
    stmt = select(func.count).where(*condations).limit(1).offset(0)
    result = (await session.execute(stmt)).scalar_one()
    print(result)