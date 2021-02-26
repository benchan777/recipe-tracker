from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from recipe_tracker_app.models import User, Recipe, Ingredients

class RecipeForm(FlaskForm):
    # category = SelectField('Category', choices = [('DESSERT', 'Dessert'), ('ENTREES', 'Entrees'), ('APPETIZERS', 'Appetizers'), ('OTHER', 'Other')])
    category = StringField('Category', validators = [DataRequired()])
    instructions = StringField('Instructions', validators = [DataRequired()])
    submit = SubmitField('Submit Recipe')

class IngredientsForm(FlaskForm):
    # category = SelectField('Category', choices = [('VEGETABLE', 'Vegetable'), ('MEAT', 'Meat'), ('DAIRY', 'Dairy'), ('GRAINS', 'Grains'), ('FRUITS', 'Fruits'), ('OILS', 'Oils'), ('FISH', 'Fish'), ('OTHER', 'Other')])
    category = StringField('Category', validators = [DataRequired()])
    name = StringField('Name', validators = [DataRequired()])
    submit = SubmitField('Submit Ingredient')