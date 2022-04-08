
from . import main
from flask import render_template,url_for,Response,flash,redirect,request, jsonify
from project.models import User,LogPost
from flask_login import current_user,login_required
from project import db
from project.utils import admin_required

from project import db
from project.models import Role, Permissions
from project.schema import UserShema

@main.route("/")
def index():
   return redirect(url_for("auth.login"))


@main.route('/admin/dashboard', methods = ['POST', 'GET'])
@admin_required
@login_required
def admin_account():
	posts = LogPost.query.all()
	users = User.query.all()

	return render_template('/main/admin.html', posts = posts,users = users, permissions = Permissions)



@main.route('/delete/log/<string:log_id>', methods = ['POST'])
@admin_required
@login_required
def delete_logs(log_id):

	log = LogPost.query.filter_by(log_id= log_id).first()

	db.delete(log)
	db.session.commit()

	return redirect( url_for('main.admin_account'))
@main.route('/edit/user/', methods = ['POST'])
@admin_required
@login_required
def edit_user():

	user_schema = UserShema()

	user_data = request.get_json(force =True)

	validate_errors = user_schema.validate(user_data)

	if validate_errors:

		return jsonify({"Error":f"{validate_errors}"}), 400

	user = User.query.filter_by(username = user_data['oldusername']).first()

	if not user_data:

		return jsonify({"Error": "No data passed"}), 400

	user.username = user_data['username']
	user.email = user_data['email']
	user.ip = user_data['ip']

	if 'role' in user_data:

		role = Role.query.filter_by(name = user_data['role']).first()

		user.role = role

	if 'password' in user_data:

		user.password = user_data['password']

	if 'status' in user_data:

		user.status = user_data['status']

	db.session.add(user)
	db.session.commit()

	return jsonify({"Message": "user details updated"}), 200


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

