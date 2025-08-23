from dao import user as user_dao
from cache import user as userCache
from domain import user as domain


class UserRepo:
    def __int__(self, dao: user_dao.UserDao, cache: userCache.UserCache):
        self.dao = dao
        self.cache = cache

    def save(self, user: domain.User):
        return self.dao.save(user)

    def get_user_by_id(self, user_id: int):
        return self.dao.get_user_by_id(user_id)