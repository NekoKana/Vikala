from typing import Tuple
import api.server
from .data_headers import DataHeaders
from .result_code import ResultCode
from .endpoint import Information, SignUp, Login
from .models.user import User
from .user_manager import UserManager
from flask import jsonify, make_response, abort

class Handler:
    def handle_information(self):
        endpoint: Information = Information(api.server.VERSION)
        return self.success(
            DataHeaders(-1, "").to_dict(ResultCode.RC_SUCCESS),
            endpoint.response()
        )

    def handle_signup(self, request: dict):
        print(request)
        endpoint: SignUp = SignUp.request(request)
        if endpoint is None:
            return self.error(ResultCode.RC_SIGNUP_ERROR, 'The field is invalied.')
        else:
            (user, token) = UserManager.generate(endpoint.name, endpoint.email, endpoint.password, endpoint.birthday, endpoint.city)
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