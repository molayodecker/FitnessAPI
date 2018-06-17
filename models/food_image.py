from flask_essentials import database

class FoodImageModel(database.Model):
    __tablename__ = 'food_image'
    id = database.Column(database.Integer, primary_key = True)
    image_name = database.Column(database.String(80), nullable = False, doc='Image name can not be null')
    image_path = database.Column(database.String(255), nullable = False)
    food_id = database.Column(database.Integer, database.ForeignKey('food.id'))
    food = database.relationship('FoodModel', backref= 'food_image')