from flask_essentials import database

""" A user model that is used to login a user into the Application """
class UserModel(database.Model):
    __tablename__ = 'users'
    id = database.Column(database.Integer, primary_key = True)
    public_id = database.Column(database.String(255), unique = True)
    username = database.Column(database.String(150), nullable= False, doc='username has to be unique and can not be empty')
    password = database.Column(database.String(255), nullable= False, doc='password can not be empty')
    admin = database.Column(database.Boolean)
    created_at = database.Column(database.Date, nullable= True)
    userprofile = database.relationship('UserProfileModel', backref='users')
    usermeasure = database.relationship('MeasurementModel', backref='users')
    usermealplan= database.relationship('MealPlanModel', backref='users')
    userphoto = database.relationship('PhotoModel', backref='users')
