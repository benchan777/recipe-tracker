import unittest
from recipe_tracker_app import app, bcrypt, db
from recipe_tracker_app.models import User, Recipe, Ingredients

# Setup
def new_user():
    password = bcrypt.generate_password_hash('password')
    user = User(username = 'ben', password = password)
    db.session.add(user)
    db.session.commit()

def login(client, username, password):
    return client.post('/login', data=dict(
        username = username,
        password = password
    ), follow_redirects = True)

def create_recipe():
    recipe = Recipe(
        name = 'Tiramisu',
        recipe = 'Tiramisu recipe here!',
        recipe_type = 'DESSERT'
    )

    db.session.add(recipe)
    db.session.commit()

# Tests
class MainTests(unittest.TestCase):
    ''' Main Tests '''

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def test_create_recipe(self):
        ''' Tests creation of new recipe '''
        create_recipe()
        new_user()
        login(self.app, 'ben', 'password')
        
        data = {
            'name': 'Cookies',
            'recipe': 'Cookies recipe here!',
            'recipe_type': 
        }

        self.app.post('/create_recipe', data = data)

        new_recipe = Recipe.query.filter_by(name = 'Cookies').one()
        self.assertIsNotNone(new_recipe)
        self.assertEqual(new_recipe.category, 'DESSERT')