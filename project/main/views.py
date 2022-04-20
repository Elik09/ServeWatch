
import json
from . import main
from flask import render_template,url_for,Response,flash,redirect,request, jsonify
from project.models import User,LogPost
from flask_login import current_user,login_required
from project import db
from project.utils import admin_required

from project import db
from project.models import Role, Permissions
from project.schema import UserShema, AddUserSchema, DeleteUserSchema

import pdb

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


@main.route('/delete/log', methods = ['POST'])
@admin_required
@login_required
def delete_logs():

	return jsonify({"Messge":"Ok"}), 200

@main.route('/register/user', methods = ["POST"])
@admin_required
@login_required
def register_user():

	user_schema = AddUserSchema()

	user_data = request.get_json(force = True)

	validate_errors = user_schema.validate(user_data)

	if validate_errors:

		return jsonify({"Error":f"{validate_errors}"}), 400

	user= User()
	user.username = user_data['username']
	user.email = user_data['email']
	user.password =  user_data['password']
	role = Role.query.filter_by(name=user_data['role']).first()
	user.role = role
	user.status = user_data['status']
	db.session.add(user)
	db.session.commit()

	return jsonify({"message":"user Created"}), 202


@main.route('/edit/user/', methods = ['POST'])
@admin_required
@login_required
def edit_user():

	user_data = request.get_json(force =True)

	if not user_data:

		return jsonify({"message":"no data was sent"}), 400


	user = User.query.filter_by(username = user_data['oldusername']).first()

	if user is None:

		return jsonify({"message":"user not not found"}), 404

	user_schema = UserShema(user)

	validate_errors = user_schema.validate(user_data)

	if validate_errors:

		return jsonify({"Error":f"{validate_errors}"}), 400


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


@main.route('/delete/user', methods = ['POST'])
@admin_required
@login_required
def delete_user():

	user_data = request.get_json(force = True)

	user_schema = DeleteUserSchema()

	errors = user_schema.validate(user_data)

	if errors:

		return jsonify({"message":errors}), 404

	user = User.query.filter_by(username= user_data['username']).first()

	db.session.delete(user)
	db.session.commit()

	return jsonify({"message":"user deleted"})

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

