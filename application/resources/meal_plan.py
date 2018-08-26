from flask_restful import Resource
from webargs.flaskparser import use_args, use_kwargs
from controllers.auth import Controller
from models.meal_plan import MealPlanModel
from schemes.meal_plan import MealPlanSchema
from helpers.auth import Tokenizer


Controller = new Controller(MealPlanModel)
class MealPlan(Resource):
    
    @Tokenizer.token_required
    def get(self, args):
        pass
    
    @use_args(MealPlanSchema(many = True))
    @Tokenizer.token_required
    def post(self, args):
        pass