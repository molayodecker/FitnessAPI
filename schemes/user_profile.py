from flask import request
from flask_essentials import database
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import Schema, fields, pre_load, post_load, pre_dump, post_dump, validates, fields, ValidationError, pprint
from models.user_profile import UserProfileModel
from models.user import UserModel
# from schemes.user import UserSchema
import jwt
from controllers.auth import Controller

class UserProfileSchema(ModelSchema):
    class Meta:
        model = UserProfileModel
        strict = True
        sqla_session = database.session

    @pre_load(pass_many = True)
    def addprofile(self, args, many):
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            data = jwt.decode(token, 'f7yD5o~5%rw28H.' , algorithms='HS256')
            user_data = Controller(UserModel).find_by_public_id(data['public_id'])
        for values in args:
            new_profile = UserProfileModel(age=values['age'],gender=values['gender'],\
            email= values['email'],weight= values['weight'],height=values['height'],\
            goal=values['goal'],calories=values['calories'],loss=values['loss'],\
            gain=values['gain'],user= user_data)
            database.session.add(new_profile)
            database.session.commit()

    