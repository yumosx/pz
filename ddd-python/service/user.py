from repositroy import user as user_repo
from domain import user as domain

class UserService:
    def __init__(self, repo: user_repo.UserRepo):
        self.repo = repo

    def register(self, user: domain.User):
        self.repo.save(user)

    def get_user(self, user_id: int):
        self.repo.get_user_by_id(user_id)