# from recipe_tracker_app.forms import
from flask import request, render_template, redirect, url_for, flash, Blueprint
from recipe_tracker_app import app, db
from recipe_tracker_app.forms import RecipeForm, IngredientsForm
from recipe_tracker_app.models import Recipe, Ingredients

main = Blueprint('main', __name__)

@main.route('/')
def homepage():
    ''' Website homepage '''
    return render_template('home.html')

@main.route('/profile')
def profile():
    ''' User profile page '''
    return render_template('profile.html')

@main.route('/create_recipe', methods = ['GET', 'POST'])
def create_recipe():
    ''' Page to create new recipes '''
    form = RecipeForm()

    if form.validate_on_submit():
        new_recipe = Recipe(
            recipe = form.instructions.data,
            recipe_type = form.category.data
        )
        db.session.add(new_recipe)
        db.session.commit()

        flash('New recipe added!')
        return redirect(url_for('main.homepage'))
        
    return render_template('create_recipe.html', form = form)

@main.route('/create_ingredient', methods = ['GET', 'POST'])
def create_ingredient():
    ''' Page to create new ingredients '''
    form = IngredientsForm()

    if form.validate_on_submit():
        new_ingredient = Ingredients(
            name = form.name.data,
            type = form.category.data
        )
        db.session.add(new_ingredient)
        db.session.commit()

        flash('New ingredient added!')
        return redirect(url_for('main.homepage'))
        
    return render_template('create_ingredient.html', form = form)