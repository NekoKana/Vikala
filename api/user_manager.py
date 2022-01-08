import random
from typing import Tuple
from .config import session
from .models.user import User
from .models.token import Token
from .models.topic import Topic
from .token_factory import TokenFactory

class UserManager:
    @classmethod
    def insert(cls, model):
        session.add(model)
        session.commit()

    @classmethod
    def delete_user(cls, user: User):
        session.query(User). \
                filter(User.viewer_id == user.viewer_id and User.user_id == user.user_id). \
                delete()
        session.commit()

    @classmethod
    def get_user_by_user_id(cls, id: int) -> User:
        user = session.query(User). \
                       filter(User.user_id == id). \
                       first()

        return user

    @classmethod
    def get_user_by_email(cls, email: str) -> User:
        user = session.query(User). \
                       filter(User.email == email). \
                       first()

        return user

    @classmethod
    def has_user_id(cls, id: int) -> bool:
        for user in cls.get_all_user():
            if user.user_id == id:
                return True
        return False

    @classmethod
    def update_user_id(cls, old_id: int, new_id: int):
        user = cls.get_user_by_user_id(old_id)
        user.user_id = new_id
        session.commit()

    @classmethod
    def has_email(cls, email: str) -> bool:
        for user in cls.get_all_user():
            if user.email == email:
                return True
        return False

    @classmethod
    def add_topic(cls, user_id: int, topic_id: int):
        topic = Topic(user_id, topic_id)
        cls.insert(topic)

    @classmethod
    def get_topics(cls, user_id: int) -> list:
        topics = session.query(Topic).filter(Topic.user_id == user_id).all()
        return topics

    @classmethod
    def validate(cls, user_id: int, token: str) -> bool:
        if cls.has_user_id(user_id):
            res = session.query(Token).filter(Token.user_id == user_id).all()
            for r in res:
                if r.token == token:
                    return True
        return False


    @classmethod
    def get_all_user(cls) -> list:
        return session.query(User).all()

    @classmethod
    def get_all_token(cls) -> list:
        return session.query(Token).all()

    @classmethod
    def login(cls, email: str, password: str) -> Tuple:
        if cls.has_email(email):
            user: User = cls.get_user_by_email(email)
            if user.password == password:
                token = Token(user.user_id, TokenFactory.generate_token())
                cls.insert(token)
                return (user, token)
        return None

    @classmethod
    def generate(cls, name: str, email: str, password: str, birthday: int, city: int, topics: list) -> Tuple:
        while True:
            user_id = random.randint(100000000, 999999999)
            if not (cls.has_user_id(user_id)):
                user = User(user_id, name, email, password, birthday, city)
                token = Token(user_id, TokenFactory.generate_token())

                for topic_id in topics:
                    cls.add_topic(user_id, topic_id)

                cls.insert(user)
                cls.insert(token)

                return (user, token)
