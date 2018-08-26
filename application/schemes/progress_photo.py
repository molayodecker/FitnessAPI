from flask_essentials import database
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import Schema, fields, pre_load, post_load, pre_dump, post_dump, validates, fields, ValidationError, pprint
from models.progress_photo import ProgressPhotoModel

class ProgressPhotoSchema(ProgressPhotoModel):
    class Meta:
        model = ProgressPhotoModel
        strict = True
        sqla_session = database.session
