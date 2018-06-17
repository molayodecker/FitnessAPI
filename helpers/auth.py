from flask import request, jsonify
from functools import wraps 
import jwt
from controllers.auth import Controller
from models.user import UserModel
from schemes.user import UserSchema
from flask_api import status

"""Helpers 

"""
class Tokenizer:

    @classmethod
    def init_app(cls, current_app):
        cls.secret_key  = current_app.secret_key

    @classmethod    
    def token_required(cls, func):
        @wraps(func)
        def decorator(*args, **kwargs):
            token = None
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']

            if not token:
                return status.HTTP_401_UNAUTHORIZED

            try:
                data = jwt.decode(token, cls.secret_key , algorithms='HS256')
                user_data = Controller(UserModel).find_by_public_id(data['public_id'])
                logged_in_user = UserSchema().dump(user_data).data
            except:
                return status.HTTP_500_INTERNAL_SERVER_ERROR
            
            return func(logged_in_user, *args, **kwargs)

        return decorator