from typing import Tuple
import api.server
from .data_headers import DataHeaders
from .result_code import ResultCode
from .endpoint import Information, SignUp, Login, GetUser, AddTopics, GetCity, \
CreateRoom, GetRoom, SearchRoomsByPrefecture, GetRoomsByUserId, GetUsersByRoomId
from .models.user import User
from .models.room import Room
from .user_manager import UserManager
from .room_manager import RoomManager
from .city_provider import CityProvider
from flask import jsonify, make_response, abort

class Handler:
    def handle_information(self):
        endpoint: Information = Information(api.server.VERSION)
        return self.success(
            DataHeaders(-1, "").to_dict(ResultCode.RC_SUCCESS),
            endpoint.response()
        )

    def handle_signup(self, request: dict):
        endpoint: SignUp = SignUp.request(request)
        if endpoint is None:
            return self.error(ResultCode.RC_SIGNUP_ERROR, 'The field is invalied.')
        else:
            (user, token) = UserManager.generate(endpoint.name, endpoint.email, endpoint.password,
                                                 endpoint.birthday, endpoint.city, endpoint.topic_list)
            endpoint.user_id = user.user_id
            endpoint.token = token.token
            return self.success(
                DataHeaders(user.user_id, token.token).to_dict(ResultCode.RC_SUCCESS),
                endpoint.response()
            )

    def handle_login(self, request: dict):
        endpoint: Login = Login.request(request)
        if endpoint is None:
            return self.error(ResultCode.RC_LOGIN_ERROR, 'The field is invalied.')
        else:
            login_result = UserManager.login(endpoint.email, endpoint.password)
            if login_result is None:
                return self.error(ResultCode.RC_LOGIN_ERROR, 'Email or password is not correct.')
            else:
                (user, token) = login_result
                endpoint.user_id = user.user_id
                endpoint.token = token.token
                return self.success(
                    DataHeaders(user.user_id, token.token).to_dict(ResultCode.RC_SUCCESS),
                    endpoint.response()
                )

    def handle_get_user(self, request: dict):
        endpoint: GetUser = GetUser.request(request)
        if endpoint is None:
            return self.error(ResultCode.RC_GET_USER_ERROR, 'The field is invalied.')
        else:
            if UserManager.validate(endpoint.user_id, endpoint.token):
                user: User = UserManager.get_user_by_user_id(endpoint.user_id)
                endpoint.name = user.name
                endpoint.email = user.email
                endpoint.birthday = user.birthday
                endpoint.city = user.city
                endpoint.topic = [topic.id for topic in UserManager.get_topics(user.user_id)]
                
                return self.success(
                    DataHeaders(user.user_id, endpoint.token).to_dict(ResultCode.RC_SUCCESS),
                    endpoint.response()
                )
            else:
                return self.error(ResultCode.RC_GET_USER_ERROR, 'Token is not corrent.')

    def handle_add_topics(self, request: dict):
        endpoint: AddTopics = AddTopics.request(request)
        if endpoint is None:
            return self.error(ResultCode.RC_GET_USER_ERROR, 'The field is invalied.')
        else:
            if UserManager.validate(endpoint.user_id, endpoint.token):
                topics_list = endpoint.topics

                for topic_id in topics_list:
                    UserManager.add_topic(endpoint.user_id, topic_id)
                    
                return self.success(
                    DataHeaders(endpoint.user_id, endpoint.token).to_dict(ResultCode.RC_SUCCESS),
                    endpoint.response()
                )
            else:
                return self.error(ResultCode.RC_GET_USER_ERROR, 'Token is not corrent.')

    def handle_get_city(self, request: dict):
        endpoint: GetCity = GetCity.request(request)
        if endpoint is None:
            return self.error(ResultCode.RC_GET_CITY_ERROR, 'The field is invalied.')
        else:
            pref_id: int = endpoint.pref_id
            cities: list = CityProvider.get_cities_by_pref_id(pref_id)
            if not cities:
                return self.error(ResultCode.RC_GET_CITY_ERROR, 'The pref_id is invalied.')
            else:
                endpoint.city = []
                for city in cities:
                    endpoint.city.append(
                        {
                            "city_id": city.city_id,
                            "city_name": city.city_name
                        }
                    )
                return self.success(
                    DataHeaders(-1, "").to_dict(ResultCode.RC_SUCCESS),
                    endpoint.response()
                )
            
    def handle_create_room(self, request: dict):
        endpoint: CreateRoom = CreateRoom.request(request)
        if endpoint is None:
            return self.error(ResultCode.RC_CREATE_ROOM_ERROR, 'The field is invalied.')
        else:
            room: Room = RoomManager.create_room(endpoint.room_name, endpoint.pref_id, endpoint.city_id,
                                                endpoint.user_id, endpoint.token, endpoint.topic_id_1,
                                                endpoint.topic_id_2, endpoint.topic_id_3, endpoint.room_description)
            if room is None:
                return self.error(ResultCode.RC_CREATE_ROOM_ERROR, 'The token is invalied.')
            else:
                endpoint.room_id = room.room_id
                return self.success(
                    DataHeaders(endpoint.user_id, endpoint.token).to_dict(ResultCode.RC_SUCCESS),
                    endpoint.response()
                )

    def handle_search_rooms_by_prefecture(self, request: dict):
        endpoint: SearchRoomsByPrefecture = SearchRoomsByPrefecture.request(request)
        if endpoint is None:
            return self.error(ResultCode.RC_CREATE_ROOM_ERROR, 'The field is invalied.')
        else:
            user_id = endpoint.user_id
            token = endpoint.token
            if UserManager.validate(user_id, token):
                rooms = RoomManager.get_rooms_by_prefecture(endpoint.pref_id)
                endpoint.rooms = rooms
                return self.success(
                    DataHeaders(endpoint.user_id, endpoint.token).to_dict(ResultCode.RC_SUCCESS),
                    endpoint.response()
                )
            else:
                return self.error(ResultCode.RC_CREATE_ROOM_ERROR, 'The token is invalied.')

    def handle_get_room(self, request: dict):
        endpoint: GetRoom = GetRoom.request(request)
        if endpoint is None:
            return self.error(ResultCode.RC_GET_ROOM_ERROR, 'The field is invalied.')
        else:
            user_id = endpoint.user_id
            token = endpoint.token
            if UserManager.validate(user_id, token):
                room = RoomManager.get_room(endpoint.room_id)
                if room is None:
                    return self.error(ResultCode.RC_GET_ROOM_ERROR, 'The room is not found.')
                else:
                    endpoint.room_name = room.room_name
                    endpoint.room_description = room.room_description
                    endpoint.pref_id = room.pref_id
                    endpoint.city_id = room.city_id
                    endpoint.topic_id_1 = room.topic_id_1
                    endpoint.topic_id_2 = room.topic_id_2
                    endpoint.topic_id_3 = room.topic_id_3

                    return self.success(
                        DataHeaders(user_id, token).to_dict(ResultCode.RC_SUCCESS),
                        endpoint.response()
                    )
            else:
                return self.error(ResultCode.RC_GET_ROOM_ERROR, 'The token is invalied.')

    def handle_get_rooms_by_user_id(self, request: dict):
        endpoint: GetRoomsByUserId = GetRoomsByUserId.request(request)
        if endpoint is None:
            return self.error(ResultCode.RC_GET_ROOMS_BY_USER_ID_ERROR, 'The field is invalied.')
        else:
            user_id = endpoint.user_id
            token = endpoint.token
            if UserManager.validate(user_id, token):
                rooms: list = RoomManager.get_rooms_by_user_id(user_id)
                if not rooms:
                    return self.error(ResultCode.RC_GET_ROOMS_BY_USER_ID_ERROR, 'The user_id is invalied.')
                else:
                    endpoint.rooms = rooms

                    return self.success(
                        DataHeaders(user_id, token).to_dict(ResultCode.RC_SUCCESS),
                        endpoint.response()
                    )
            else:
                return self.error(ResultCode.RC_GET_ROOM_ERROR, 'The token is invalied.')

    def handle_get_users_by_room_id(self, request: dict):
        endpoint: GetUsersByRoomId = GetUsersByRoomId.request(request)
        if endpoint is None:
            return self.error(ResultCode.RC_GET_USERS_BY_ROOM_ID_ERROR, 'The field is invalied.')
        else:
            user_id = endpoint.user_id
            token = endpoint.token
            if UserManager.validate(user_id, token):
                users: list = RoomManager.get_users_by_room_id(endpoint.room_id)
                if not users:
                    return self.error(ResultCode.RC_GET_ROOMS_BY_USER_ID_ERROR, 'The room_id is invalied.')
                else:
                    endpoint.users = users

                    return self.success(
                        DataHeaders(user_id, token).to_dict(ResultCode.RC_SUCCESS),
                        endpoint.response()
                    )
            else:
                return self.error(ResultCode.RC_GET_ROOM_ERROR, 'The token is invalied.')


    def handle_404(self):
        return self.error(404, "Not found")

    def success(self, data_headers: dict, data: dict):
        return self.response({
            'data_headers': data_headers,
            'data': data
        }, 200)

    def error(self, result_code: int, message: str):
        return self.response({
            'data_headers': DataHeaders(-1, "").to_dict(result_code),
            'data': message
        }, 400)

    def response(self, data: dict, http_status: int):
        return make_response(jsonify(data), http_status, {"Content-Type": "application/json"})