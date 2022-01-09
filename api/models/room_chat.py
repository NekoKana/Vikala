from sqlalchemy import Column, Integer, String, Float, DateTime
from api.config import Model

class RoomChat(Model):

    __tablename__ = 'room_chat'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    room_id = Column('room_id', Integer, nullable=False)
    member_id = Column('member_id', Integer, nullable=False)
    text = Column('text', String(255), nullable=False)
    timestamp = Column('timestamp', Integer, nullable=False)

    def __init__(self, room_id: int, member_id: int, text: str, timestamp: int):
        self.room_id = room_id
        self.member_id = member_id
        self.text = text
        self.timestamp = timestamp