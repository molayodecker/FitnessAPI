""" This is the main application.
    The building blocks of this application which will be broken into different parts for the API
    Application, Helper, Model, Controller, Schema, Resource
"""

from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import Schema, fields, pre_load, post_load, pre_dump, post_dump, validates, fields, ValidationError, pprint
from webargs import fields, missing
from webargs.flaskparser import use_args, use_kwargs
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp, generate_password_hash, check_password_hash
import datetime
import uuid
import jwt
from models.user import UserModel
from models.user_profile import UserProfileModel
from models.progress_photo import ProgressPhotoModel
from models.photo import PhotoModel
from models.measurement import MeasurementModel
from models.food import FoodModel
from models.food_image import FoodImageModel
from models.meal_plan import MealPlanModel
from models.meal_category import MealCategoryModel
from schemes.user_profile import UserProfileSchema
from controllers.auth import Controller
from helpers.auth import Tokenizer
from flask_essentials import database, marshmallow
from resources.user import User, UserList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database.init_app(app)
marshmallow.init_app(app)
app.secret_key = 'f7yD5o~5%rw28H.'
Tokenizer.init_app(app)
api = Api(app)


class PhotoSchema(ModelSchema):
    class Meta:
        model = PhotoModel
        strict = True
        sqla_session = database.session


class ProgressPhotoSchema(ModelSchema):
    class Meta:
        model = ProgressPhotoModel
        strict = True
        sqla_session = database.session


class MeasurementSchema(ModelSchema):
    class Meta:
        model = MeasurementModel
        strict = True
        sqla_session = database.session


class FoodSchema(ModelSchema):
    class Meta:
        model = FoodModel
        strict = True
        sqla_session = database.session


class MealPlanSchema(ModelSchema):
    class Meta:
        model = MealPlanModel
        strict = True
        sqla_session = database.session


class FoodImageSchema(ModelSchema):
    class Meta:
        model = FoodImageModel
        strict = True
        sqla_session = database.session

    
class MealCategorySchema(ModelSchema):
    class Meta:
        model = MealCategoryModel
        strict = True
        sqla_session = database.session


       

class UserProfile(Resource):
    @Tokenizer.token_required
    def get(self, logged_in_user):
        if self['public_id']:
            print('Cont')
        else:
            raise ValueError('Unable to verify user')

    
    @use_args(UserProfileSchema(many = True))
    @Tokenizer.token_required
    def post(self,logged_in_user,args):
        # print(self)
        temp = Controller(UserModel).find_by_public_id(self['public_id'])
        # if self['public_id']:
        #     new_profile = UserProfileModel(age=10,gender="Female",email= "dominique@morgan.com",weight= 140,height=5.7,goal=120,calories=1200,loss=20,gain=40,user_id= self['id'])
        #     database.session.add(new_profile)
        #     database.session.commit()




class UserLogin(Resource):
    def get(self):
        auth = request.authorization
        print('i am {} '.format(auth))
        if not auth or not auth.username or not auth.password:
            return make_response('Could not Verify', 401, {'WWW-Authenicate': 'Basic-realm = "Login-required!"'})

        user = Controller(UserModel).find_by_username(username = auth.username)

        print('The user is {}'.format(user))
        
        if not user:
            return make_response('Could not Verify', 401, {'WWW-Authenicate': 'Basic-realm = "Login-required!"'})
        
        if check_password_hash(user.password, auth.password):
            token = jwt.encode({'public_id': user.public_id, 'expire': str(datetime.datetime.utcnow() + datetime.timedelta(minutes = 30))}, app.secret_key, algorithm='HS256')
            print(token.decode('UTF-8'))
            return jsonify({'token': token.decode('UTF-8')})
        
        return make_response('Could not Verify', 401, {'WWW-Authenicate': 'Basic-realm = "Login-required!"'})


"""" User Authentication 
     -------------------

"""

def authenticate(username, password):
    user = Controller(UserModel).find_by_username(username)
    if user and check_password_hash(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return Controller(UserModel).find_by_id(user_id)

flask_jwt = JWT(app, authenticate, identity)


@app.before_request
def create_table():
    database.create_all()
    # create_user = UserModel(username = 'Matt', password = 'hughs')
    # database.session.add(create_user)
    # user_scheme = UserSchema()
    # data = user_scheme.dump(create_user).data
    # print(data)
    


"""
        RESOURCES
        ---------
Api endpoints 

"""
api.add_resource(UserList, '/create_user')
api.add_resource(User, '/user')
api.add_resource(UserProfile, '/profile')
api.add_resource(UserLogin, '/login')



if __name__ == '__main__':
    app.run(port=5000, debug=True)