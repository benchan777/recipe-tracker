# from recipe_tracker_app.forms import
from flask import request, render_template, redirect, url_for, flash, Blueprint
from flask_login import current_user
from recipe_tracker_app import app, db
from recipe_tracker_app.forms import RecipeForm, IngredientsForm
from recipe_tracker_app.models import Recipe, Ingredients, User

main = Blueprint('main', __name__)

@main.route('/')
def homepage():
    ''' Website homepage '''
    saved_recipes = Recipe.query.all()
    return render_template('home.html', saved_recipes = saved_recipes)

@main.route('/profile/<user_id>')
def profile(user_id):
    ''' User profile page '''
    user = User.query.filter_by(id = user_id).one()
    recipes = Recipe.query.filter_by(id = user_id).all()
    return render_template('profile.html', user = user, recipes = recipes)

@main.route('/create_recipe', methods = ['GET', 'POST'])
def create_recipe():
    ''' Page to create new recipes '''
    form = RecipeForm()

    if form.validate_on_submit():
        new_recipe = Recipe(
            name = form.name.data,
            recipe = form.instructions.data,
            recipe_type = form.category.data,
            creator_id = current_user.id
        )
        db.session.add(new_recipe)
        db.session.commit()

        flash('New recipe added!')
        return redirect(url_for('main.recipe_detail', recipe_id = new_recipe.id))
        
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

@main.route('/recipe_detail/<recipe_id>', methods = ['GET', 'POST'])
def recipe_detail(recipe_id):
    ''' Displays details of the recipe '''
    recipe = Recipe.query.get(recipe_id)
    # form = IngredientsForm(obj = recipe)

    # if form.validate_on_submit():


    return render_template('recipe_detail.html', recipe = recipe)

