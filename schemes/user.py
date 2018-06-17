from flask_essentials import database
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import Schema, fields, pre_load, post_load, pre_dump, post_dump, validates, fields, ValidationError, pprint
from webargs import fields, missing
from webargs.flaskparser import use_args, use_kwargs
from models.user import UserModel
from werkzeug.security import safe_str_cmp, generate_password_hash, check_password_hash
import uuid
from controllers.auth import Controller
import datetime
from schemes.user_profile import UserProfileSchema

class UserSchema(ModelSchema):
    user_profile = fields.Nested(UserProfileSchema, many = True)

    class Meta:
        model = UserModel
        strict = True
        sqla_session = database.session

    """
    user creation
    ---------------
    The marshmallow decorator @pre_load is being used here to intercept
    the data, in order to salt the password. Before commiting
    the data into the database
    We are also setting many to true because we expect more than 
    one value from post

    Bug: The function can not check if database already exist
    """
    @pre_load(pass_many =  True)
    def create_user(self, args, many):
        username , password = ... , ...
        for values in args:
            username = values['username']
            password = generate_password_hash(values['password'], method='sha256')
            public_id = str(uuid.uuid4())
            payload  = [{'public_id': public_id, 'username': username, 'password': password, 'admin': False ,'created_at': str(datetime.date.today()) }]
            print(payload)
            # user = UserSchema().dump(Controller(UserModel).find_by_username(username)).data 
            # if user == {}:
            #     return payload, 200
            # elif user is not None and user['username']:
            #     raise ValidationError('{} already exist'.format(user['username']))
        return [{'public_id': public_id, 'username': username, 'password': password, 'admin': False ,'created_at': str(datetime.date.today()) }]


    @pre_dump(pass_many = True)
    def get_user(self, args, many):
        pass      