from slutools import db, login_manager
from slutools import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=100), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=30))
    name = db.Column(db.String(length=50))
    group = db.Column(db.String(length=50), nullable=False)
    active = db.Column(db.String(length=1), nullable=False)