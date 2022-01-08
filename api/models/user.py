from sqlalchemy import Column, Integer, String, Float, DateTime
from api.config import Model

class User(Model):

    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer, nullable=False)
    name = Column('name', String(40), nullable=False)
    email = Column('email', String(40), nullable=False)
    password = Column('password', String(40), nullable=False)
    birthday = Column('birthday', Integer, nullable=True)
    city = Column('city', Integer, nullable=True)

    def __init__(self, user_id: int, name: str, email: str, password: str, birthday: int, city: int):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.birthday = birthday
        self.city = city