from sqlalchemy import Column, Integer, String, Float, DateTime
from api.config import Model

class Prefecture(Model):

    __tablename__ = 'prefecture'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    pref_id = Column('pref_id', Integer, nullable=False)
    pref_name = Column('pref_name', String(20), nullable=False)



    def __init__(self, pref_id: int, pref_name: str):
        self.pref_id = pref_id
        self.pref_name = pref_name
