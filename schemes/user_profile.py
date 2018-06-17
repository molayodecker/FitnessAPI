from flask_essentials import database
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import Schema, fields, pre_load, post_load, pre_dump, post_dump, validates, fields, ValidationError, pprint
from models.user_profile import UserProfileModel

class UserProfileSchema(ModelSchema):
    class Meta:
        model = UserProfileModel
        strict = True
        sqla_session = database.session

    @pre_load(pass_many = True)
    def addprofile(self, args, many):
        pass
        # for values in args:
        #     new_profile = UserProfileModel(age=values['age'],gender=values['gender'],email= values['email'],weight= values['weight'],height=values['height'],goal=values['goal'],calories=values['calories'],loss=values['loss'],gain=values['gain'],user_id= self['id'])

    