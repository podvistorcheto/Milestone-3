import os
import bcrypt
import base64 
from base64 import b64encode
from flask import Flask, render_template, redirect, request, url_for, session
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path



if path.exists("env.py"):
    import env

app = Flask(__name__)


app.config["MONGO_DBNAME"] = "cooking_book"
app.config["MONGO_URI"] = os.getenv('MONGO_URI')


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


mongo = PyMongo(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grid_recipes')
def grid_recipes():
    return render_template("grid_recipes.html")

@app.route('/profile')
def profile():
    if 'email' in session:
        return render_template('profile.html').format(session["email"])
    else:
        return render_template('login.html')

""" login form with user fetching with mongodb """

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_email = users.find_one({'name' : request.form['email']})
        if login_email:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_email['password']) == login_email['password']:
                session['email'] = request.form['email']
                return redirect(url_for('profile'))
        return 'Invalid email/password combination'
    else:
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users
        """existing_email = users.find_one({'name' : request.form['email']})"""
        existing_email = users.find_one({'name' : request.form['email']})

        if existing_email is None:
            """create encoded object before hashing the password form"""
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            """ and store the hashed version of the password"""
            users.insert_one({'name' : request.form['email'], 'password' : hashpass})
            session['email'] = request.form['email']
            return redirect(url_for('profile'))
        return 'This username and/or email already exists!'

    return render_template('signup.html')


""""@app.route('/logout')
def logout():
    return 'Log out successfull'"""

@app.route('/share_recipe')
def share_recipe():
    return render_template('share_recipe.html', recipes=mongo.db.recipes.find())

@app.route('/upload', methods=['POST'])
def upload_recipe():
    image = request.files['image']       
    image_string = "data:image/png;base64," + base64.b64encode(image.read()).decode("utf-8")
    recipes = mongo.db.recipes
    recipe = request.form.to_dict()
    recipe['image'] = image_string
    recipes.insert_one(recipe)
    manage_upload = request.form.to_dict()
    if manage_upload is None:
        return 'Please fill in all fields!'
    return redirect(url_for('meals'))


""" create route for the html form to upload files"""
@app.route('/file_upload')
def file_upload():
        return render_template("upload_photo.html")


""" connect the function to upload the picture to mongodb collection """
@app.route('/create', methods=['POST'])
def create():
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.photos.insert_one({'username' : request.form.get('username'), 'profile_image_name' : profile_image.filename})
    
    return render_template('findphoto.html', photos=mongo.db.photos.find())


""" retrieve pic from mongodb step 1 - creates an endpoint that allows you to retreive data from"""
@app.route('/gallery/<filename>')
def gallery(filename):
    return mongo.send_file(filename)

"""step 2 call the file from the endpoint to display for the user"""
@app.route('/user_a/<username>')
def user_a(username):
     user_a = mongo.db.photos.find_one_or_404({'username': username})
     return f'''
        <img src="{url_for('gallery', filename=user_a['profile_image_name'])}">
        '''


@app.route('/meals')
def meals():
    return render_template('meals.html', recipes=mongo.db.recipes.find())

@app.route('/review_meals/<meal_id>')
def review_meals(meal_id):
    the_review = mongo.db.recipes.find_one({"_id": ObjectId(meal_id)})
    reviews_data = mongo.db.reviews.find({'name': the_review['name']})
    return render_template("modify.html", recipes=the_review, reviews=reviews_data)

@app.route('/upload_review', methods=['POST'])
def upload_review():
    reviews = mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    manage_review = request.form.to_dict()
    if manage_review is None:
        return 'Please fill in all fields!'
    return redirect(url_for('meals'))


@app.route('/carta')
def carta():
    return render_template('view_recipe.html', recipes=mongo.db.recipes.find())


@app.route('/delete_recipe/<meal_id>')
def delete_recipe(meal_id):
    mongo.db.recipes.delete_one({'_id': ObjectId(meal_id)})
    return redirect(url_for('meals'))


if __name__ == '__main__':
    app.secret_key = 'gatanka'
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)