from recipe_tracker_app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    ''' User information model '''
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable = False, unique = True)
    password = db.Column(db.String(80), nullable = False)
    user_ingredients = db.relationship('Ingredients', secondary = 'user_ingredients_table', back_populates = 'users_with_ingredient')

class Recipe(db.Model):
    ''' Recipe model '''
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    recipe = db.Column(db.Text(), nullable = False)
    recipe_type = db.Column(db.String(80), nullable = False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # recipe_ingredients = 

class Ingredients(db.Model):
    ''' Ingredients model '''
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    type = db.Column(db.String(80), nullable = False)
    users_with_ingredient = db.relationship('User', secondary = 'user_ingredients_table', back_populates = 'user_ingredients')

user_ingredients_table = db.Table('user_ingredients_table',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id')),
)