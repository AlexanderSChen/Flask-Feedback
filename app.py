from flask import Flask, render_template, redirect, session, flash 
from flask_debugtoolbar import DebugToolbarExtension 
from models import connect_db, db, User, Tweet 
from forms import UserForm, TweetForm 
from sqlalchemy.exc import IntegrityError 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask_feedback"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
app.config["SQLALCHEMY_ECHO"] = True 
app.config["SECRET_KEY"] = "SECRETAFKEY"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False 

connect_db(app)

toolbar = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return redirect('/register')

@app.route('/register', methods=["GET", "POST"])
def register_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        new_user = User.register(username, password, email, first_name, last_name)

        db.session.add(new_user)

        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append('Username taken. Please pick another')
            form.email.errors.append('This email is already associated with an existing account')
            return render_template('register.html', form = form)
        
        session['username'] = new_user.username
        flash('Welcome! Account Successfully Created!', 'success')
        return redirect('/secret')