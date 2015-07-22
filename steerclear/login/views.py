from flask import Blueprint, flash, render_template, url_for, redirect
from flask.ext.login import login_user, logout_user, login_required
from flask_restful import abort
from sqlalchemy import exc
from steerclear import login_manager
from forms import *
from models import *

# setup login blueprint
login_bp = Blueprint('login', __name__)

"""
user_loader
-----------
Returns a user given the (unicode) user_id.
this needs to be implemented for flask-login extension to work
"""
@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

"""
login
-----
main endpoint for logging users in and out
GET - returns the login page
POST - logs user in if valid username and password
       and redirects to index page else returns the login template
:TODO: factor in password hashing + salt. add
       more helpful error messages
"""
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('driver_portal.index'))
    return render_template('login.html', action=url_for('.login'))

"""
logout
------
Logs out the user. User must already be logged in, else
return 401. Once user is logged out, redirect to login page
"""
@login_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))

@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        try:
            db.session.add(new_user)
            db.session.commit()
        except exc.IntegrityError:
            flash('user already exists')
            return render_template('login.html', action=url_for('.register'))
            abort(404)
        return redirect(url_for('.login'))
    return render_template('login.html', action=url_for('.register'))

@login_bp.route('/test_login')
@login_required
def test_login():
    return "Congrats, you are logged in"
