from sqlalchemy import Column, Integer, String, Float, DateTime
from api.config import Model

class City(Model):

    __tablename__ = 'city'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    city_id = Column('city_id', Integer, nullable=False)
    pref_id = Column("pref_id", Integer, nullable=False)
    city_name = Column('city_name', String(50), nullable=False)

    def __init__(self, city_id: int, pref_id: int, city_name: str):
        self.city_id = city_id
        self.pref_id = pref_id
        self.city_name = city_name
