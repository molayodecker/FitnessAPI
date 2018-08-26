from flask_essentials import database
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import Schema, fields, pre_load, post_load, pre_dump, post_dump, validates, fields, ValidationError, pprint
from models.food_image import FoodImageModel

class FoodImageModel(ModelSchema):
    class Meta:
        model = FoodImageModel
        strict = True
        sqla_session =database.session