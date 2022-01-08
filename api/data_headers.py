import time

class DataHeaders:
    def __init__(self, user_id: int, token: str):
        self.__user_id = user_id
        self.__token = token

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token

    def to_dict(self, result_code: int):
        return {
            'user_id': self.user_id,
            'token': self.token,
            'timestamp': int(time.time()),
            'result_code': result_code
        }

