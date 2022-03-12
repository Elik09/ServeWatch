from crypt import methods
from . import main
from flask import render_template,url_for,Response,flash,redirect,request
from project.models import User,Post
from flask_login import current_user,login_required
from project.utils import admin_required


@main.route("/")
def index():
   return redirect(url_for("auth.login"))


@main.route('/admin/account', methods = ['POST', 'GET'])
@admin_required
@login_required
def admin_account():

	return "admin account"

@main.route('/account')
@login_required
def account():

	posts = Post.query.all()

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

