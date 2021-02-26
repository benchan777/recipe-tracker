from recipe_tracker_app import Config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_object(Config)

# Initialize authentication
bcrypt = Bcrypt(app)
login = LoginManager()
login.login_view = 'auth.login'
login.init_app(app)

# Initialize database
db = SQLAlchemy(app)