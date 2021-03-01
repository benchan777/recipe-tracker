from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
# from recipe_tracker_app.models import User, Recipe, Ingredients

class RecipeForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    category = SelectField('Category', choices = [('DESSERT', 'Dessert'), ('ENTREES', 'Entrees'), ('APPETIZERS', 'Appetizers'), ('OTHER', 'Other')])
    instructions = TextAreaField('Instructions', validators = [DataRequired()])
    submit = SubmitField('Submit Recipe')

class IngredientsForm(FlaskForm):
    category = SelectField('Category', choices = [('VEGETABLES', 'Vegetable'), ('MEAT', 'Meat'), ('DAIRY', 'Dairy'), ('GRAINS', 'Grains'), ('FRUITS', 'Fruits'), ('OILS', 'Oils'), ('FISH', 'Fish'), ('OTHER', 'Other')])
    name = StringField('Name', validators = [DataRequired()])
    submit = SubmitField('Submit Ingredient')