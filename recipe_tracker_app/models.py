from recipe_tracker_app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    ''' User information model '''
    id = db.Column(db.String(80), primary_key = True)
    username = db.Column(db.String(80), nullable = False, unique = True)
    password = db.Column(db.String(80), nullable = False)