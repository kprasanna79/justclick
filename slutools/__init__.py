from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager #  identify user ID that is stored in their session cookie


app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://kumaravelp:India123@localhost:3306/just_click'
app.config['SECRET_KEY'] = 'ae22be78d7bc65f23d5cb808'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"

from slutools import routes