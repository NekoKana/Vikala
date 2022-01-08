from sqlalchemy import Column, Integer, String, Float, DateTime
from api.config import Model

class Token(Model):

    __tablename__ = 'token'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer, nullable=False)
    token = Column('token', String(50), nullable=False)

    def __init__(self, user_id: int, token: str):
        self.user_id = user_id
        self.token = token
