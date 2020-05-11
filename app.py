import os
from flask import Flask, render_template, redirect, request, url_for, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
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
def index():
    return render_template('render.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
        return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup_post():
    #code to validate and add user to database goes here
    users = mongo.db.users
    users.insert_one(request.form.to_dict())

    """user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))"""


    return redirect(url_for('login'))



@app.route('/logout')
def logout():
    return 'Log out successfull'

@app.route('/share_recipe')
def share_recipe():
    return render_template('share_recipe.html', recipes=mongo.db.recipes.find())

@app.route('/upload_recipe', methods=['POST'])
def upload_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('meals'))


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