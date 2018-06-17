from flask_essentials import database

class MealPlanModel(database.Model):
    __tablename__ = 'meal'
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(150), nullable = False)
    date = database.Column(database.DateTime)
    notes = database.Column(database.String(255))
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    user_meal = database.relationship('UserModel', backref= 'meal')