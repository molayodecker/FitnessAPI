from flask_essentials import database 

""" Photo Model stores the profile photo of the user 
    A user may have one or no photo
    By default a user is given a default animated photo or given
    the possibility to choose one
"""
class PhotoModel(database.Model):
    __tablename__ = 'photo'
    id = database.Column(database.Integer, primary_key = True)
    image_name = database.Column(database.String(80), nullable = False, doc='Image name can not be null')
    image_path = database.Column(database.String(255), nullable = False)
    posted_at = database.Column(database.Date, nullable= False)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'), nullable=False)
    userphoto = database.relationship('UserModel', backref= 'photo')