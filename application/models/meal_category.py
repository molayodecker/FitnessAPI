from flask_essentials import database

class MealCategoryModel(database.Model):
    __tablename__ = 'meal_category'
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(150))
    meal_plan_id = database.Column(database.Integer, database.ForeignKey('meal.id'))
    meal_plan_cat = database.relationship('MealPlanModel', backref = 'meal_category')