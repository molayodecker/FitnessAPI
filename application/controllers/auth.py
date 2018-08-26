from flask_essentials import database
from flask import jsonify
from marshmallow.exceptions import ValidationError as MarshmallowValidationError
from sqlalchemy.exc import SQLAlchemyError

""" Controller """   
class Controller():

    def __init__(self,model):
        self.model = model 
    
    def find_all_usernames(self, username):
        pass

    def find_by_username(self,username):
        return self.model.query.filter_by(username = username).one_or_none()

    def find_by_id(self,id):
        return self.model.query.filter_by(id = id).first()

    def find_by_public_id(self,public_id):
        return self.model.query.filter_by(public_id = public_id).first()

    def find_all(self,param):
        return self.model.query.filter_by(user_id = param).all()


    def save_to_database(self,args):
        try:
            database.session.add_all(args)
            database.session.commit()
        except MarshmallowValidationError as error:
            raise error
        except SQLAlchemyError as error:
            database.session.rollback()
            raise error

    def save_none_iter_to_database(self,args):
        try:
            database.session.add(args)
            database.session.commit()
        except MarshmallowValidationError as error:
            raise error
        except SQLAlchemyError as error:
            database.session.rollback()
            raise error