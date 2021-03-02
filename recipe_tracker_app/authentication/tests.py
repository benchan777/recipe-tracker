from unittest import TestCase
from recipe_tracker_app import app, bcrypt, db
from recipe_tracker_app.models import User, Recipe, Ingredients

# Setup
def new_user():
    user = User(username = 'ben', password = password)
    password = bcrypt.generate_password_hash('password')
    db.session.add(user)
    db.session.commit()

# Tests
class AuthTests(TestCase):
    """Tests for authentication (login & signup)."""

    def setUp(self):
        """Executed prior to each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def signup(self):
        ''' Test signup route '''
        user_data = {
            'username': 'test_user',
            'password': 'password'
        }
        self.app.post('/signup', data = user_data)

        