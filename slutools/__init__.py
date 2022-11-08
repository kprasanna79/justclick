from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager #  identify user ID that is stored in their session cookie


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://kumaravelp:India123@localhost:3306/flask_market'
app.config['SECRET_KEY'] = 'ae22be78d7bc65f23d5cb808'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from slutools import routes