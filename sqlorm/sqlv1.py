import sqlalchemy
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, sessionmaker

Base = declarative_base()

db = sqlalchemy.create_engine("")
session = sessionmaker(bind=db)
base = declarative_base()

class User(Base):
    __tablename__ = "users"
    # 这个 mapped_column 表示当前的
    id: Mapped[int] = mapped_column(primary_key=True)