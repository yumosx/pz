class UserDao:
    def __int__(self, db):
        self.db = db

    def get_user_by_id(self, id):
        return self.db.get(id)

    def save(self, user):
        return self.db.save(user)