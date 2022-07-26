from wsgiref import validate
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField 
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    username = StringField(
        "Username", 
        validators=[InputRequired(), Length(min=1, max=20)]
    )
    password = PasswordField(
        "Password", 
        validators=[InputRequired(), Length(min=6, max=55)]
    )
    email = StringField(
        "Email", 
        validators=[InputRequired(), Length(max=50)]
    )
    first_name = StringField(
        "First Name", 
        validators=[InputRequired(), Length(max=30)]
    )
    last_name = StringField(
        "Last Name", 
        validators=[InputRequired(), Length(max=30)]
    )

class LoginForm(FlaskForm):
    """Form for logging in a registered user."""

    username = StringField(
        "Username", 
        validators=[InputRequired(), Length(min=1, max=20)]
    )
    password = PasswordField(
        "Password", 
        validators=[InputRequired(), Length(min=6, max = 55)]
    )

class FeedbackForm(FlaskForm):
    """Form for adding feedback"""

    title = StringField(
        "Title",
        validators=[InputRequired()]
    )
    content = StringField(
        "Content",
        validators=[InputRequired()]
    )

class DeleteForm(FlaskForm):
    """Intentionally Blank"""