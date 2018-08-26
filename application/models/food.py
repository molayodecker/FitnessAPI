from flask_essentials import database

class FoodModel(database.Model):
    __tablename__ = 'food'
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(80), nullable = True)
    food_type = database.Column(database.String(80))
    carbohydrates = database.Column(database.Float)
    protein = database.Column(database.Float)
    fat = database.Column(database.Float)
    fiber = database.Column(database.Float)
    calcium = database.Column(database.Float)
    iron = database.Column(database.Float)
    zinc = database.Column(database.Float)
    sodium = database.Column(database.Float)
    calories = database.Column(database.Float)
    quantity = database.Column(database.Float)
    unit = database.Column(database.Float)