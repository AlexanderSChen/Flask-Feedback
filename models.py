from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt 

db = SQLAlchemy()

bcrypt = Bcrypt()

def connect_db(app):
    """Connects to our database"""

    db.app = app 
    db.init_app(app)

class User(db.Model):
    __tablename__ = "users"

    username = db.Column(
        db.String(20), 
        primary_key = True, 
        nullable = False, 
        unique = True
    )
    password = db.Column(db.Text, nullable = False)
    email = db.Column(db.String(50), nullable = False, unique = True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)

    feedback = db.relationship('Feedback', backref = "users", cascade = "all,delete")

    @classmethod
    def to_dict(self):
        """Return User Data"""
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }

    @classmethod 
    def register(cls, username, password, email, first_name, last_name):
        """Register user with hashed password and return user"""

        # turn password into bcrypt encrypted bytestring with random salt
        hashed = bcrypt.generate_password_hash(password)

        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")

        user =cls(
            username=username,
            password=hashed_utf8,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        
        db.session.add(user)
        return user

    @classmethod 
    def authenticate(cls, username, pwd):
        """Validate that user exists and password is correct.
        
        Return user if valid; else return false."""

        u = User.query.filter_by(username = username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u 
        else:
            return False 

class Feedback(db.Model):
    """Feedback class"""
    __tablename__ = 'feedback'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False)
    username = db.Column(db.String(20), db.ForeignKey('users.username'), nullable = False)
