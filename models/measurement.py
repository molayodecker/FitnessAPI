from flask_essentials import database

""" Help the user to measure:
    waist, hips and arms
    during weight losing journey
"""
class MeasurementModel(database.Model):
    __tablename__ = 'measurement'
    id = database.Column(database.Integer, primary_key = True)
    waist = database.Column(database.Integer)
    hips = database.Column(database.Integer)
    arms = database.Column(database.Integer)
    posted_at = database.Column(database.DateTime)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    user_measurement = database.relationship('UserModel', backref= 'measurement')