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
from resources.measurement import Measurement
from resources.user_profile import UserProfile
from resources.photo import Photo


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database.init_app(app)
marshmallow.init_app(app)
app.secret_key = 'f7yD5o~5%rw28H.'
Tokenizer.init_app(app)
api = Api(app)

    
class MealCategorySchema(ModelSchema):
    class Meta:
        model = MealCategoryModel
        strict = True
        sqla_session = database.session


       
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
api.add_resource(Measurement,'/measurement')
api.add_resource(Photo, '/photo')



if __name__ == '__main__':
    app.run(port=5000, debug=True)