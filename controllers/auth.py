from flask import jsonify

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

    def save_to_database(args):
        database.session.add_all(args)
        database.commit()