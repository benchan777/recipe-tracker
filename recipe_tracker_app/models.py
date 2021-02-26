from recipe_tracker_app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    ''' User information model '''
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable = False, unique = True)
    password = db.Column(db.String(80), nullable = False)

class Recipe(db.Model):
    ''' Recipe model '''
    id = db.Column(db.Integer, primary_key = True)
    recipe = db.Column(db.Text(), nullable = False)
    recipe_type = db.Column(db.String(80), nullable = False)
    # recipe_ingredients = 

class Ingredients(db.Model):
    ''' Ingredients model '''
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    type = db.Column(db.String(80), nullable = False)

# ingredients_table = db.Table('user_ingredients',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'))
# )