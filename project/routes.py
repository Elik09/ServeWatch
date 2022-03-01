from flask import render_template,url_for,Response,flash,redirect,request
from project import app,db,bcrypt
from project.models import User,Post
from project.forms import RegistrationForm, LoginForm

users=[
	{
		"username" : "testing", 
		"password" : "testingpass",
		"email" : "testing@gmail.com"
	}
] 


@app.route("/")
def index():
   return render_template('index.html',title="Index")

@app.route("/home")
def home():
   return render_template('home.html',title="Home")


@app.route("/about")
def about():
	return render_template('about.html',title="About")

# @app.route("/readme")
@app.route("/README.md")
def readme():
	resp=Response(open('project/static/docs/README.md','r').read())
	resp.headers['Content-Type']="text/plain; charset=utf-8"
	return resp

def hashpassword(password):
	return bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()

@app.route('/register',methods=['GET','POST']) 
def register():
	form=RegistrationForm()
	if form.validate_on_submit():
		hashed_password=hashpassword(form.password.data)
		user=User(username=form.username.data,email=form.email.data,password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created for {form.username.data} with password {hashed_password}! Login now','success')
		return redirect(url_for('login'))

	else:
		return render_template('register.html',title="Register",form=form)

@app.route('/login',methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		for user in users:
			if (user.get('email','None') == form.email.data):
				flash(f'Logged In {form.email.data}!','success')
				return redirect(url_for('home'))
			else:
				pass
		flash(f'Login Failed for  : {form.email.data}! Please check your username and password','fail')
		return redirect(url_for('login'))
	else:
		return render_template('login.html',title="Login Page",form=form)



