from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from recipe_tracker_app.models import User
from recipe_tracker_app import bcrypt

class Signup(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 3, max = 40)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 3)])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class Login(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 3, max = 40)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 3)])
    submit = SubmitField('Log In')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()

        if not user:
            raise ValidationError('That username does not exist. Please try again.')

    def validate_password(self, password):
        user = User.query.filter_by(username = self.username.data).first()

        if user and not bcrypt.check_password_hash(user.password, password.data):
            raise ValidationError('Incorrect password. Please try again.')