from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from slutools.models import User

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class RegisterForm(FlaskForm):
    username = StringField(label='Slunet_id:', validators=[Length(min=6, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    name = StringField(label='Name:', validators=[Length(min=6, max=30), DataRequired()])
    group = StringField(label='Group:', validators=[Length(min=6, max=30), DataRequired()])
    active = StringField(label='Active:', validators=[Length(min=1, max=2), DataRequired()])
