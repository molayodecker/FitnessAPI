from flask_restful import Resource
from helpers.auth import Tokenizer
from schemes.user_profile import UserProfileSchema
from models.user import UserModel

class UserProfile(Resource):
    @Tokenizer.token_required
    def get(self, logged_in_user):
        if self['public_id']:
            print('Cont')
        else:
            raise ValueError('Unable to verify user')

    
    @use_args(UserProfileSchema(many = True))
    @Tokenizer.token_required
    def post(self,logged_in_user,args):
        pass