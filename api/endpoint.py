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
