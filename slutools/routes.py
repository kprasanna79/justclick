from slutools import app, login_manager
from flask import render_template, request, redirect, url_for, flash
from slutools.models import User
from flask_login import login_user


@app.route('/profile')
def profile_page():
    return render_template('profile.html')



@app.route('/login', methods=['GET', 'POST'])
def login_page():
    print ("Inside login route")
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if user:
        login_user(user)
        print(f'The Logged in user is : {email}, {password}')
        return redirect(url_for('profile_page'))
    else:
        return render_template('login.html')