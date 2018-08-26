from flask_essentials import database
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import Schema, fields, pre_load, post_load, pre_dump, post_dump, validates, fields, ValidationError, pprint
from models.meal_plan import MealPlanModel

class MealPlanSchema(ModelSchema):
    class Meta:
        model = MealPlanModel
        strict = true
        sqla_session = database.session