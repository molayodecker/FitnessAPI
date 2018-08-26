from flask import jsonify
from flask_restful import Resource
from models.user import UserModel
from models.user_profile import UserProfileModel
from schemes.user import UserSchema
from helpers.auth import Tokenizer
from controllers.auth import Controller
from webargs.flaskparser import use_args, use_kwargs
from flask_essentials import database

comtroller = Controller(UserModel) 
class User(Resource):
    @Tokenizer.token_required
    def get(self, logged_in_user):
        user = Controller(UserModel).find_by_public_id(self['public_id'])
        if not user:
            return jsonify({ 'message': 'No user found'})
        user_data = UserSchema().dump(user).data  
        return [{ **user_data }]


class UserList(Resource):
    @Tokenizer.token_required
    def get(self, logged_in_user):
        return jsonify({'message': 'Hello'})
       

    @use_args(UserSchema(many = True))
    def post(self, args):
        database.session.add_all(args)
        database.session.commit()