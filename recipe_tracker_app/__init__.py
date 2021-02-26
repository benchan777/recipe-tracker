from recipe_tracker_app.config import Config
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

# Blueprints
from recipe_tracker_app.routes import main
app.register_blueprint(main)

from recipe_tracker_app.authentication.routes import authentication
app.register_blueprint(authentication)

# Create Database
with app.app_context():
    db.create_all()