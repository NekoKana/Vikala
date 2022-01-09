import api.server
from api.data_headers import DataHeaders
from api.exception import InvaliedTypeException

class Get:
    def response(self):
        pass

    @classmethod
    def http_method(cls):
        return ['GET']

class Post(Get):
    @classmethod
    def request(cls, dic: dict):
        pass

    @classmethod
    def http_method(cls):
        return ['POST']

class Information(Get):
    version: float

    def __init__(self, version):
        self.version = version

    def response(self):
        return {
            'version': self.version
        }


class SignUp(Post):
    name: str
    user_id: int
    email: str
    password: str
    birthday: int
    city: int
    topic_list: list
    token: str

    def __init__(self, name: str, email: str, password: str, birthday: int, city: int, topic_list: list):
        self.name = name
        self.email = email
        self.password = password
        self.birthday = birthday
        self.city = city
        self.topic_list = topic_list

    def response(self):
        return {
            'user_id': self.user_id,
            'token': self.token
        }

    @classmethod
    def request(cls, dic: dict):
        try:
            return SignUp(name=Validator.validate_str(dic['name']),
                          email=Validator.validate_str(dic['email']),
                          password=Validator.validate_str(dic['password']),
                          birthday=Validator.validate_int(dic['birthday']),
                          city=Validator.validate_int(dic['city']),
                          topic_list=Validator.validate_list(dic['topic_list']))
        except KeyError:
            return None
        except TypeError:
            return None
        except InvaliedTypeException:
            return None

class Login(Post):
    user_id: int
    email: str
    password: str
    token: str

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def response(self):
        return {
            'user_id': self.user_id,
            'token': self.token
        }

    @classmethod
    def request(cls, dic: dict):
        try:
            return Login(email=Validator.validate_str(dic['email']),
                          password=Validator.validate_str(dic['password']))
        except KeyError:
            return None
        except TypeError:
            return None
        except InvaliedTypeException:
            return None

class GetUser(Post):
    user_id: int
    token: str
    name: str
    email: str
    birthday: int
    city: int
    topic: list

    def __init__(self, user_id: int, token: str):
        self.user_id = user_id
        self.token = token

    def response(self):
        return {
            "name": self.name,
            "user_id": self.user_id,
            "email": self.email,
            "birthday": self.birthday,
            "city": self.city,
            "topic": self.topic
        }

    @classmethod
    def request(cls, dic: dict):
        try:
            return GetUser(user_id=Validator.validate_int(dic['user_id']),
                          token=Validator.validate_str(dic['token']))
        except KeyError:
            return None
        except TypeError:
            return None
        except InvaliedTypeException:
            return None

class AddTopics(Post):
    user_id: int
    token: str
    topics: list

    def __init__(self, user_id: int, token: str, topics: list):
        self.user_id = user_id
        self.token = token
        self.topics = topics

    def response(self):
        return []

    @classmethod
    def request(cls, dic: dict):
        try:
            return AddTopics(user_id=Validator.validate_int(dic['user_id']),
                          token=Validator.validate_str(dic['token']),
                          topics=Validator.validate_list(dic['topics']))
        except KeyError:
            return None
        except TypeError:
            return None
        except InvaliedTypeException:
            return None

class GetCity(Post):
    pref_id: int
    city: list

    def __init__(self, pref_id: int):
        self.pref_id = pref_id

    def response(self):
        return {
            'city': self.city
        }

    @classmethod
    def request(cls, dic: dict):
        try:
            return GetCity(pref_id=Validator.validate_int(dic['pref_id']))
        except KeyError:
            return None
        except TypeError:
            return None
        except InvaliedTypeException:
            return None

class CreateRoom(Post):
    room_id: int
    room_name: str
    room_description: str
    pref_id: int
    city_id: int
    topic_id_1: int
    topic_id_2: int
    topic_id_3: int

    user_id: int
    token: str

    def __init__(self, room_name: str, room_description: str, pref_id: int, city_id: int, 
                topic_id_1: int, topic_id_2: int, topic_id_3: int, user_id: int, token: str):
        self.room_name = room_name
        self.room_description = room_description
        self.pref_id = pref_id
        self.city_id = city_id
        self.topic_id_1 = topic_id_1
        self.topic_id_2 = topic_id_2
        self.topic_id_3 = topic_id_3

        self.user_id = user_id
        self.token = token

    def response(self):
        return {
            'room_id': self.room_id
        }

    @classmethod
    def request(cls, dic: dict):
        try:
            room_description = None

            if 'room_description' in dic:
                room_description = Validator.validate_str(dic['room_description'])

            topic_id_1 = Validator.validate_int(dic['topic_id_1'])
            topic_id_2 = None
            topic_id_3 = None

            if 'topic_id_2' in dic:
                topic_id_2 = Validator.validate_int(dic['topic_id_2'])

            if 'topic_id_3' in dic:
                topic_id_3 = Validator.validate_int(dic['topic_id_3'])

            return CreateRoom(room_name=Validator.validate_str(dic['room_name']),
                            room_description=room_description,
                            pref_id=Validator.validate_int(dic['pref_id']),
                            city_id=Validator.validate_int(dic['city_id']),
                            topic_id_1=topic_id_1,
                            topic_id_2=topic_id_2,
                            topic_id_3=topic_id_3,
                            user_id=Validator.validate_int(dic['user_id']),
                            token=Validator.validate_str(dic['token']))
        except KeyError:
            return None
        except TypeError:
            return None
        except InvaliedTypeException:
            return None

class SearchRoomsByPrefecture(Post):
    rooms: list
    pref_id: int

    user_id: int
    token: str

    def __init__(self, pref_id: int, user_id: int, token: str):
        self.pref_id = pref_id
        self.user_id = user_id
        self.token = token

    def response(self):
        return {
            'rooms': self.rooms
        }

    @classmethod
    def request(cls, dic: dict):
        try:
            return SearchRoomsByPrefecture(pref_id=Validator.validate_int(dic['pref_id']),
                            user_id=Validator.validate_int(dic['user_id']),
                            token=Validator.validate_str(dic['token']))
        except KeyError:
            return None
        except TypeError:
            return None
        except InvaliedTypeException:
            return None

class SearchRoomsByCity(Post):
    rooms: list
    city_id: int

    user_id: int
    token: str

    def __init__(self, city_id: int, user_id: int, token: str):
        self.city_id = city_id
        self.user_id = user_id
        self.token = token

    def response(self):
        return {
            'rooms': self.rooms
        }

    @classmethod
    def request(cls, dic: dict):
        try:
            return SearchRoomsByCity(city_id=Validator.validate_int(dic['city_id']),
                            user_id=Validator.validate_int(dic['user_id']),
                            token=Validator.validate_str(dic['token']))
        except KeyError:
            return None
        except TypeError:
            return None
        except InvaliedTypeException:
            return None

class GetRoom(Post):
    room_name: str
    room_id: int
    room_description: str
    pref_id: int
    city_id: int
    topic_id_1: int
    topic_id_2: int
    topic_id_3: int

    user_id: int
    token: str

    def __init__(self, room_id: int, user_id: int, token: str):
        self.room_id = room_id
        self.user_id = user_id
        self.token = token

    def response(self):
        return {
            'room_id': self.room_id,
            'room_name': self.room_name,
            'room_description': self.room_description,
            'pref_id': self.pref_id,
            'city_id': self.city_id,
            'topic_id_1': self.topic_id_1,
            'topic_id_2': self.topic_id_2,
            'topic_id_3': self.topic_id_3
        }

    @classmethod
    def request(cls, dic: dict):
        try:
            return GetRoom(room_id=Validator.validate_int(dic['room_id']),
                            user_id=Validator.validate_int(dic['user_id']),
                            token=Validator.validate_str(dic['token']))
        except KeyError:
            return None
        except TypeError:
            return None
        except InvaliedTypeException:
            return None

class JoinRoom(Post):
    room_id: int
    user_id: int
    token: str

    def __init__(self, room_id: int, user_id: int, token: str):
        self.room_id = room_id
        self.user_id = user_id
        self.token = token

    def response(self):
        return []

    @classmethod
    def request(cls, dic: dict):
        try:
            return JoinRoom(room_id=Validator.validate_int(dic['room_id']),
                            user_id=Validator.validate_int(dic['user_id']),
                            token=Validator.validate_str(dic['token']))
        except KeyError:
            return None
        except TypeError:
            return None
        except InvaliedTypeException:
            return None


class GetRoomsByUserId(Post):
    rooms: list
    user_id: int
    token: str

    def __init__(self, user_id: int, token: str):
        self.user_id = user_id
        self.token = token

    def response(self):
        return self.rooms

    @classmethod
    def request(self, dic: dict):
        try:
            return GetRoomsByUserId(user_id=Validator.validate_int(dic['user_id']),
                                    token=Validator.validate_str(dic['token']))
        except KeyError:
            return None
        except TypeError:
            return None
        except InvaliedTypeException:
            return None

class GetUsersByRoomId(Post):
    room_id: int
    users: list
    
    user_id: int
    token: str

    def __init__(self, room_id: int, user_id: int, token: str):
        self.room_id = room_id
        self.user_id = user_id
        self.token = token

    def response(self):
        return self.users

    @classmethod
    def request(self, dic: dict):
        try:
            return GetUsersByRoomId(room_id=Validator.validate_int(dic['room_id']),
                                    user_id=Validator.validate_int(dic['user_id']),
                                    token=Validator.validate_str(dic['token']))
        except KeyError:
            return None
        except TypeError:
            return None
        except InvaliedTypeException:
            return None

class RenameRoom(Post):
    room_id: int
    new_name: str

    user_id: int
    token: str

    def __init__(self, room_id: int, new_name: str, user_id: int, token: str):
        self.room_id = room_id
        self.new_name = new_name
        self.user_id = user_id
        self.token = token

    def response(self):
        return []

    @classmethod
    def request(cls, dic: dict):
        try:
            return RenameRoom(room_id=Validator.validate_int(dic['room_id']),
                            new_name=Validator.validate_str(dic['new_name']),
                            user_id=Validator.validate_int(dic['user_id']),
                            token=Validator.validate_str(dic['token']))
        except KeyError:
            return None
        except TypeError:
            return None
        except InvaliedTypeException:
            return None

class GetChatHistory(Post):
    room_id: int
    count: int
    history: list

    user_id: int
    token: str

    def __init__(self, room_id: int, count: int, user_id: int, token: str):
        self.room_id = room_id
        self.count = count
        self.user_id = user_id
        self.token = token

    def response(self):
        return {
            "history": self.history
        }

    @classmethod
    def request(cls, dic: dict):
        try:
            return GetChatHistory(room_id=Validator.validate_int(dic['room_id']),
                                count=Validator.validate_int(dic['count']),
                                user_id=Validator.validate_int(dic['user_id']),
                                token=Validator.validate_str(dic['token']))
        except KeyError:
            return None
        except TypeError:
            return None
        except InvaliedTypeException:
            return None

class Validator:
    @classmethod
    def validate_int(cls, i: int):
        if type(i) == int:
            return i
        else:
            raise InvaliedTypeException('%s is not int' % type(i))

    @classmethod
    def validate_str(cls, s: str):
        if type(s) == str:
            return s
        else:
            raise InvaliedTypeException('%s is not str' % type(s))

    @classmethod
    def validate_float(cls, f: float):
        if type(f) == float:
            return f
        else:
            raise InvaliedTypeException('%s is not float' % type(f))

    @classmethod
    def validate_list(cls, l: list):
        if type(l) == list:
            return l
        else:
            raise InvaliedTypeException('%s is not list' % type(l))

    @classmethod
    def validate_dict(cls, d: dict):
        if type(d) == dict:
            return d
        else:
            raise InvaliedTypeException('%s is not dict' % type(d))

    @classmethod
    def validate_bool(cls, b: bool):
        if type(b) == bool:
            return b
        else:
            raise InvaliedTypeException('%s is not bool' % type(b))
