from flask import request, jsonify
from flask_restful import Resource
from helpers.auth import Tokenizer
from webargs.flaskparser import use_args, use_kwargs
from controllers.auth import Controller
from flask_essentials import database
from models.photo import PhotoModel
from schemes.photo import PhotoScheme
from models.user import UserModel
import datetime 

controller = Controller(PhotoModel)
class Photo(Resource):
    
    @use_args(PhotoScheme(many = True))
    @Tokenizer.token_required
    def post(self, logged_in_user, args):

        # Grab the form and file data.
        form_data = request.form.to_dict()
        file_data = request.files.to_dict()
        file_storage_key = [file_key for file_key in file_data.keys()][0]
        file_storage = file_data[file_storage_key]

        # Get the file_type: file_storage.content_type is something like 'image/png'.
        file_type = file_storage.content_type[ file_storage.content_type.find( '/' ) + 1: ]
        print(file_type)
        file_name = f"{self['public_id']}.{file_type}"

        print(file_name)
        
    
