from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    def __init__(self):
        pass

    @staticmethod
    def register(session: AsyncSession):
        pass

    @staticmethod
    async def login(cls, session : AsyncSession):
        pass

    @staticmethod
    async def get_user_info(session: AsyncSession, user_id: int):
        if id:
            raise ValueError("id 参数不能为空")