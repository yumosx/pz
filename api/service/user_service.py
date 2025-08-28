from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import  select
from api.mappers.user_mapper import User as UserMapper


class UserService:
    def __init__(self):
        pass

    @classmethod
    def register(cls, session: AsyncSession):
        pass

    @classmethod
    async def login(cls, session : AsyncSession):
        pass

    @classmethod
    async def get_user_info(cls, session: AsyncSession, user_id: int):
        if id:
            raise ValueError("id 参数不能为空")

        stmt = select(UserMapper).where(UserMapper.id == user_id)
        session.execute(stmt)
        pass