from flask_essentials import database
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import Schema, fields, pre_load, post_load, pre_dump, post_dump, validates, fields, ValidationError, pprint
from webargs import fields, missing
from webargs.flaskparser import use_args, use_kwargs
from models.measurement import  MeasurementModel


class MeasurementSchema(ModelSchema):
    class Meta:
        model = MeasurementModel
        strict = True
        sqla_session = database.session

    @pre_load(pass_many = True)
    def test(self,args, many):
        return args

