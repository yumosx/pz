import sqlalchemy as sa

engine = sa.create_engine("sqlite:///:memory")
connection = engine.connect()

metadata = sa.MetaData()

# 数据库的model 定义
user_table = sa.Table(
    "user",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("username", sa.String),
    sa.Column("email", sa.String),
)

metadata.create_all(engine)

def insert_user(username : str, email: str):
    query = user_table.insert().values(username=username, email=email)
    connection.execute(query)


def select_user(username: str):
    query = user_table.select().where(user_table.c.username == username)
    result = connection.execute(query)
    return result.fetchone()

def main() ->None:
    metadata.create_all(engine)
    insert_user("", "")
    connection.close()