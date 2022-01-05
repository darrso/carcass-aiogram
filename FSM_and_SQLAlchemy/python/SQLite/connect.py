from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine("sqlite:///python/SQLite/users.db", echo=True)
base = declarative_base()


class User(base):
    __tablename__ = 'users'

    Id = Column(Integer, primary_key=True)
    TgId = Column(Integer, unique=True)
    Name = Column(String)
    Old = Column(String)
    Living = Column(String)


base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()