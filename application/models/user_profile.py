from flask_essentials import database

""" A user profile  Model stores information about the user
    Fields created are:
    id, age, gender, email, weight, height, goal, calories, loss, gain
"""
class UserProfileModel(database.Model):
    __tablename__ = 'user_profile'
    id = database.Column(database.Integer, primary_key = True)
    age = database.Column(database.Integer, nullable = False)
    gender =  database.Column(database.String(10), nullable = False)
    email = database.Column(database.String(150), nullable = False)
    weight = database.Column(database.Integer, nullable = False)
    height = database.Column(database.Integer)
    goal = database.Column(database.Integer)
    calories = database.Column(database.Integer)
    loss = database.Column(database.Integer)
    gain = database.Column(database.Integer)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'), nullable=False)
    
     # define relationship
    user = database.relationship('UserModel', backref= 'user_profile')