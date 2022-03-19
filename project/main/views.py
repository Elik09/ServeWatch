
from . import main
from flask import render_template,url_for,Response,flash,redirect,request
from project.models import User,LogPost
from flask_login import current_user,login_required
from project import db
from project.utils import admin_required
from .forms import LogEditForm, UserEditForm

@main.route("/")
def index():
   return redirect(url_for("auth.login"))


@main.route('/admin/account', methods = ['POST', 'GET'])
# @admin_required
# @login_required
def admin_account():
	posts = LogPost.query.all()

	return render_template('/main/admin.html', posts = posts)

@main.route('/edit/logs/<string:log_id>', methods = ['POST'])
@admin_required
@login_required
def edit_logs(log_id):

	logEditform = LogEditForm()

	return "edit"

@main.route('/delete/log/<string:log_id>', methods = ['POST'])
@admin_required
@login_required
def delete_logs(log_id):

	log = LogPost.query.filter_by(log_id= log_id).first()

	db.delete(log)
	db.session.commit()

	return redirect( url_for('main.admin_account'))
@main.route('/admin/edit/accounts', methods = ["POST", "GET"])
# @admin_required
# @login_required
def edit_accounts():

	users = User.query.all()

	return render_template('/main/edit.html', users = users)


@main.route('/edit/user/<string:username>', methods = ['POST'])
@admin_required
@login_required
def edit_user(username):

	user = User.query.filter_by(username = username).first()

	userForm = UserEditForm()

	return redirect( url_for('main.edit_accounts'))

@main.route('/delete/user/<string:username>', methods = ['POST'])
@admin_required
@login_required
def delete_user(username):

	user = User.query.filter_by(username= username).first()

	db.delete(user)
	db.session.commit()

	return redirect( url_for('main.edit_accounts'))

@main.route('/account')
@login_required
def account():

	posts = LogPost.query.all()

	return render_template('/main/account.html', posts = posts)



@main.route("/about")
def about():
	return render_template('about.html',title="About")

# @app.route("/readme")
@main.route("/README.md")
def readme():
	resp=Response(open('README.md','r').read())
	resp.headers['Content-Type']="text/plain; charset=utf-8"
	return resp

