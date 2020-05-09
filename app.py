import os
from flask import Flask, render_template, redirect, request, url_for, Blueprint
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path



if path.exists("env.py"):
    import env

app = Flask(__name__)


app.config["MONGO_DBNAME"] = "cooking_book"
app.config["MONGO_URI"] = os.getenv('MONGO_URI')


mongo = PyMongo(app)

main = Blueprint('main', __name__)


@app.route('/')
@app.route('/main_page')
def main_page():
    return render_template("index.html", recipes=mongo.db.recipes.find())

@app.route('/profile')
def profile():
    return 'Profile'

@app.route('/login')
def login():
    return 'Login'

@app.route('/signup')
def signup():
    return 'Signup'

@app.route('/logout')
def logout():
    return 'Logout'

@app.route('/share_recipe')
def share_recipe():
    return render_template('share_recipe.html', recipes=mongo.db.recipes.find())

@app.route('/upload_recipe', methods=['POST'])
def upload_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('share_recipe'))


@app.route('/meals')
def meals():
    return render_template('meals.html', recipes=mongo.db.recipes.find())

@app.route('/carta')
def carta():
    return render_template('recipe_list.html', recipes=mongo.db.recipes.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)