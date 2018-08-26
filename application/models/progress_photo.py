from flask_essentials import database


""" Helps the user to take progress photos during the users weight loss journey """
class ProgressPhotoModel(database.Model):
    __tablename__ = 'progress_photo'
    id = database.Column(database.Integer, primary_key = True)
    image_name = database.Column(database.String(80), nullable = False, doc='Image name can not be null')
    image_path = database.Column(database.String(255), nullable = False)
    posted_at = database.Column(database.DateTime, nullable= False)
