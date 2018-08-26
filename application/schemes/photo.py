from flask import request
from flask_essentials import database
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import Schema, fields, pre_load, post_load, pre_dump, post_dump, validates, fields, ValidationError, pprint
from models.photo import PhotoModel

class PhotoScheme(ModelSchema):
    class Meta:
        model = PhotoModel
        strict = True
        sqla_session = database.session

    # @pre_load(pass_many =  True)
    # def getphoto(self, args, many):
    #     pass