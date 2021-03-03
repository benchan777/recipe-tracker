from unittest import TestCase
from recipe_tracker_app import app, bcrypt, db
from recipe_tracker_app.models import User, Recipe, Ingredients

# Setup
def new_user():
    user = User(username = 'ben', password = password)
    password = bcrypt.generate_password_hash('password')
    db.session.add(user)
    db.session.commit()

def new_recipe():
    pass