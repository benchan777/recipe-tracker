import unittest
from recipe_tracker_app import app, bcrypt, db
from recipe_tracker_app.models import User, Recipe, Ingredients

# Setup
def new_user():
    password = bcrypt.generate_password_hash('password')
    user = User(username = 'ben', password = password)
    db.session.add(user)
    db.session.commit()

# Tests
class AuthTests(unittest.TestCase):
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

        user = User.query.filter_by(username = 'test_user').one()
        self.assertIsNotNone(user)

    def login_test(self):
        ''' Test login route '''
        new_user()

        data = {
            'username': 'ben',
            'password': 'password'
        }
        self.app.post('/login', data = data)

        response = self.app.get('/', follow_redirects = True)
        self.assertIn('Log Out', response.get_data(as_text = True))


    def login_wrong_pw(self):
        ''' Test logging in with incorrect password '''
        new_user()

        data = {
            'username': 'ben',
            'password': 'wrong_password'
        }

        response = self.app.post('/login', data = data)
        self.assertIn('Incorrect password. Please try again.', response.get_data(as_text = True))

    def login_nonexistent_username(self):
        ''' Test logging in with nonexistent username '''
        new_user()

        data = {
            'username': 'jaldhfjaafj',
            'password': 'password'
        }

        response = self.app.post('/login', data = data)
        self.assertIn('That username does not exist. Please try again.', response.get_data(as_text = True))

    def logout_test(self):
        ''' Test logging out '''
        new_user()

        data = {
            'username': 'ben',
            'password': 'password'
        }

        self.app.post('/login', data = data)

        response = self.app.get('/logout', follow_redirects = True)
        self.assertNotIn('Log Out', response.get_data(as_text = True))