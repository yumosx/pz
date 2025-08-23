class UserCache:
    def __int__(self, rdb):
        self.rdb = rdb

    def set(self):
        self.rdb.set()

def build_key(value)->str:
    return f"code:{value}"