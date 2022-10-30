from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager #  identify user ID that is stored in their session cookie


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slutools.db'
app.config['SECRET_KEY'] = 'ae22be78d7bc65f23d5cb808'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from slutools import routes