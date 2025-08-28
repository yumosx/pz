import injector

class DataBase:
    def __int__(self):
        print("构造 db 成功")

    def get_name(self) -> str:
        return "wyz"

class Cache:
    def __init__(self):
        print("构造 cache 成功")

class UserDao:
    @injector.inject
    def __init__(self, db: DataBase):
        self.db = db

    def get_name(self):
        return self.db.get_name()


class UserRepo:
    @injector.inject
    def __init__(self, dao: UserDao):
        self.dao = dao
    def get_name(self)->str:
        return self.dao.get_name()


class UserService:
    @injector.inject
    def __init__(self, repo: UserRepo):
        self.repo = repo

    def get_name(self)->str:
        return self.repo.get_name()

class Provider(injector.Module):
    @injector.provider
    @injector.singleton
    def provide_db(self) ->DataBase:
        return DataBase()

    @injector.provider
    @injector.singleton
    def provider_cache(self) ->Cache:
        return Cache()

if __name__ == "__main__":
    inj = injector.Injector([Provider()])
    svc = inj.get(UserService)
    print(svc.get_name())