from sqlalchemy import Column, Integer, String, Float, DateTime
from api.config import Model

class City(Model):

    __tablename__ = 'city'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column('city_id', Integer, nullable=False)
    city_name = Column('city_name', String(50), nullable=False)

    def __init__(self, user_id: int, city_name: str):
        self.user_id = user_id
        self.city_name = city_name
