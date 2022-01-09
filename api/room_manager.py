import random

from .config import session
from .models.room import Room
from .models.user import User
from .models.room_chat import RoomChat
from .models.room_member import RoomMember
from .user_manager import UserManager
from sqlalchemy import desc

class RoomManager:
    @classmethod
    def insert(cls, model):
        session.add(model)
        session.commit()

    @classmethod
    def get_room(cls, room_id: int) -> Room:
        room: Room = session.query(Room). \
                    filter(Room.room_id == room_id). \
                    first()
        return room

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
        members = cls.get_members(room_id)
        if not members is None:
            for member in members:
                if member.user_id == user_id:
                    session.delete(member)
                    session.commit()
                    return True
        return False

    @classmethod
    def get_rooms_by_user_id(cls, user_id: int) -> list:
        members = session.query(RoomMember).all()
        rooms = []

        for member in members:
            if member.member_id == user_id:
                room: Room = cls.get_room(member.room_id)
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
    def get_users_by_room_id(cls, room_id: int) -> list:
        members = session.query(RoomMember).all()
        users = []

        for member in members:
            if member.room_id == room_id:
                user: User = UserManager.get_user_by_user_id(member.member_id)
                users.append({
                    "name": user.name,
                    "user_id": user.user_id,
                    "birthday": user.birthday,
                    "city": user.city,
                })
        return users


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
    def get_rooms_by_city(cls, city_id: int) -> list:
        rooms = []
        for room in cls.get_all_rooms():
            if room.city_id == city_id:
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
                
    @classmethod
    def get_chat_history(cls, room_id: int, count: int):
        res = []
        chats = session.query(RoomChat). \
                        filter(RoomChat.room_id == room_id). \
                        order_by(desc(RoomChat.timestamp)). \
                        limit(count). \
                        all()
                        
        for chat in chats:
            res.append({
                "member_id": chat.member_id,
                "text": chat.text,
                "timestamp": chat.timestamp
            })

        return res