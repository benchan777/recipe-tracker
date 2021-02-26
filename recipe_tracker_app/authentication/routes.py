from recipe_tracker_app import app, db, bcrypt, login
from recipe_tracker_app.models import User
from recipe_tracker_app.forms import Signup, Login
from flask import Blueprint, request, render_template, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user

authentication = Blueprint('authentication', __name__)

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@authentication.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = Signup()