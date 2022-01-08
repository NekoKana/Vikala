import random
from typing import Tuple
from .config import session
from .models.user import User
from .models.token import Token
from .token_factory import TokenFactory

class UserManager:
    @classmethod
    def insert(cls, user: User):
        session.add(user)
        session.commit()

    @classmethod
    def delete(cls, user: User):
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
        for user in cls.get_all():
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
        for user in cls.get_all():
            if user.email == email:
                return True
        return False

    @classmethod
    def get_all(cls) -> list:
        return session.query(User).all()

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
    def generate(cls, name: str, email: str, password: str, birthday: int, city: int) -> Tuple:
        while True:
            user_id = random.randint(100000000, 999999999)
            if not (cls.has_user_id(user_id)):
                user = User(user_id, name, email, password, birthday, city)
                token = Token(user_id, TokenFactory.generate_token())
                cls.insert(user)
                cls.insert(token)

                return (user, token)
