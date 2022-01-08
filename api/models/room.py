from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql.expression import null
from api.config import Model

class Room(Model):

    __tablename__ = 'room'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    room_id = Column('room_id', Integer, nullable=False)
    room_name = Column('room_name', String(50), nullable=False)
    room_description = Column('room_description', String(255), nullable=False, default="")
    pref_id = Column('pref_id', Integer, nullable=False)
    city_id = Column('city_id', Integer, nullable=False)
    topic_id_1 = Column('topic_id_1', Integer, nullable=False)
    topic_id_2 = Column('topic_id_2', Integer, nullable=True)
    topic_id_3 = Column('topic_id_3', Integer, nullable=True)


    def __init__(self, room_id: int, room_name: str, pref_id: int, city_id: int,
                topic_id_1: int, topic_id_2: int = None, topic_id_3: int = None, room_description: str = None):
        self.room_id = room_id
        self.room_name = room_name
        self.room_description = room_description
        self.pref_id = pref_id
        self.city_id = city_id
        self.topic_id_1 = topic_id_1

        if not topic_id_2 is None:
            self.topic_id_2 = topic_id_2

        if not topic_id_3 is None:
            self.topic_id_3 = topic_id_3
