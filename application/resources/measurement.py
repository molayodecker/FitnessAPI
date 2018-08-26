from flask import jsonify
from flask_restful import Resource
from helpers.auth import Tokenizer
from webargs.flaskparser import use_args, use_kwargs
from controllers.auth import Controller
from models.measurement import MeasurementModel
from schemes.measurement import MeasurementSchema
from models.user import UserModel

controller = Controller(MeasurementModel)
class Measurement(Resource):
    @Tokenizer.token_required
    def get(self, logged_in_user):
        get_measurement_model = controller.find_by_id(self['id'])
        measurement_data = MeasurementSchema().dump(get_measurement_model).data
        return [{**measurement_data}]

    @use_args(MeasurementSchema(many = True))
    @Tokenizer.token_required
    def post(self,logged_in_user, args):
        controller.save_to_database(args)
