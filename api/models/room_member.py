from sqlalchemy import Column, Integer, String, Float, DateTime
from api.config import Model

class RoomMember(Model):

    __tablename__ = 'room_member'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    room_id = Column('room_id', Integer, nullable=False)
    member_id = Column('member_id', Integer, nullable=False)

    def __init__(self, room_id: int, member_id: int):
        self.room_id = room_id
        self.member_id = member_id
