import random

from .config import session
from .models.room import Room
from .models.room_member import RoomMember
from .user_manager import UserManager

class RoomManager:
    @classmethod
    def insert(cls, model):
        session.add(model)
        session.commit()

    @classmethod
    def delete_room(cls, room_id: int) -> bool:
        room: Room = session.query(Room). \
                    filter(Room.room_id == room_id). \
                    first()
        if cls.has_room(room_id):
            session.delete(room)
            session.commit()
            return True
        else:
            return False

    @classmethod
    def rename_room(cls, room_id: int, room_name: str) -> bool:
        room: Room = session.query(Room).filter(Room.room_id == room_id).first()
        if cls.has_room(room_id):
            room.room_name = room_name
            session.commit()
            return True
        else:
            return False

    @classmethod
    def set_room_description(cls, room_id: int, room_description: str) -> bool:
        room: Room = session.query(Room).filter(Room.room_id == room_id).first()
        if cls.has_room(room_id):
            room.room_description = room_description
            session.commit()
            return True
        else:
            return False

    @classmethod
    def get_members(cls, room_id: int) -> list:
        room_member: RoomMember = session.query(RoomMember).\
                                filter(RoomMember.room_id == room_id).\
                                all()
        return room_member

    @classmethod
    def kick_member(cls, room_id: int, user_id: int) -> bool:
        members = cls.get_members()
        if not members is None:
            for member in members:
                if member.user_id == user_id:
                    session.delete(member)
                    session.commit()
                    return True
        return False

    @classmethod
    def has_room(cls, room_id: int) -> bool:
        room: Room = session.query(Room).filter(Room.room_id == room_id).first()
        return not room is None

    @classmethod
    def join_room(cls, room_id: int, user_id: int) -> bool:
        if cls.has_room(room_id):
            member: RoomMember = RoomMember(room_id, user_id)
            cls.insert(member)
            return True
        else:
            return False

    @classmethod
    def get_all_rooms(cls) -> list:
        return session.query(Room).all()

    @classmethod
    def get_rooms_by_prefecture(cls, pref_id: int) -> list:
        rooms = []
        for room in cls.get_all_rooms():
            if room.pref_id == pref_id:
                rooms.append({
                    'room_id': room.room_id,
                    'room_name': room.room_name,
                    'room_description': room.room_description,
                    'pref_id': room.pref_id,
                    'city_id': room.city_id,
                    'topic_id_1': room.topic_id_1,
                    'topic_id_2': room.topic_id_2,
                    'topic_id_3': room.topic_id_3
                })
        return rooms

    @classmethod
    def create_room(cls, room_name: str, pref_id: int, city_id: int, user_id: int, token: str, 
                    topic_id_1: int, topic_id_2: int = None, topic_id_3: int = None, room_description: str = None) -> Room:
        if UserManager.validate(user_id, token):
            while True:
                room_id = random.randint(100000000, 999999999)
                if not cls.has_room(room_id):
                    room: Room = Room(room_id, room_name, pref_id, city_id, topic_id_1, topic_id_2, topic_id_3, room_description)
                    cls.insert(room)
                    cls.join_room(room_id, user_id)
                    return room
        return None
                