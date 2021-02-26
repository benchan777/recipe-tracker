from recipe_tracker_app.forms import
from flask import request, render_template, redirect, url_for, flash, Blueprint
from recipe_tracker_app import app, db

main = Blueprint('main', __name__)

@main.route('/')
def homepage():
    ''' Website homepage '''
    return render_template('home.html')

def profile():
    ''' User profile page '''
    pass