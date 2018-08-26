from flask_essentials import database
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import Schema, fields, pre_load, post_load, pre_dump, post_dump, validates, fields, ValidationError, pprint
from models.food import FoodModel

class FoodSchema(FoodModel):
    class Meta:
        model = FoodModel
        strict = True
        sqla_session = database.session