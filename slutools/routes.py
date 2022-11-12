from slutools import app, login_manager, db
from flask import render_template, request, redirect, url_for, flash
from slutools.forms import LoginForm
from slutools.models import User
from flask_login import login_user, logout_user, login_required


@app.route('/')
@app.route('/home')
@login_required
def home_page():
    return render_template('home.html')

@app.route('/sfxwalk_admin')
@login_required
def sfxwalk_page():
    return render_template('sfxwalk.html')

@app.route('/register')
def register_user_page():
    return render_template('user-addition-page.html')

@app.route('/profile')
def profile_page():
    return render_template('profile.html')



@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        print(f"The logged in user is {attempted_user.username}")
        if attempted_user: #( #and attempted_user.check_password_correction(
        #         attempted_password=form.password.data
        # ):
            login_user(attempted_user)
            flash(f"Success! You are logged in as: {attempted_user.username}", category='success')
            return redirect(url_for('home_page'))
        else:
            flash(f'Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("login_page"))