from slutools import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(length=100), nullable=False, unique=True)
    password = db.Column(db.String(length=100))
    name = db.Column(db.String(length=1000))
    group = db.Column(db.String(length=100), nullable=False)
    active = db.Column(db.String(length=1), nullable=False)