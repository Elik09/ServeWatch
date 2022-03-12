from flask import render_template,url_for,Response,flash,redirect,request
from project import db
from project.models import User
from project.utils import admin_required
from .forms import RegistrationForm, LoginForm
from flask_login import login_user,logout_user, login_required

from . import auth

# this route requires, login and admin privileges
@auth.route('/register',methods=['GET','POST']) 
@admin_required
@login_required
def register():

	form = RegistrationForm()
	return render_template('register.html',title="Register", form = form)

@auth.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():

		user = User.query.filter_by(email  = form.email.data).first()
		# 
		if user is not None and user.verify_password(form.password.data):

			login_user(user)

			next = request.args.get('next')
		
			if next is None or not next.startswith('/'):

				return redirect(url_for('main.account')) if not user.is_admin() else redirect(url_for('main.admin_account'))

			return redirect(next)

		flash("Invalide username or password")

	return render_template('auth/login.html',title="Login Page", form  = form)
		


# requires login status to access as a user can only log out if they are aready logged in
@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash(f'Logged Out!','fail')
	return redirect(url_for('auth.login'))

# this route requires login status to access
