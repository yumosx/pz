import User

class UserRepo:
    def __int__(self, dao):
        self.dao = dao
        pass

    def save(self, user: User):
        return self.dao.save()

    def get_user_by_id(self):
        return self.dao.get_user_by_id()