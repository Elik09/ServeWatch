from flask import Flask,render_template,url_for,Response,flash,redirect,request

from forms import RegistrationForm, LoginForm

app = Flask(__name__)
# Setting a secret key
app.config['SECRET_KEY'] = 'bed2a11b4ddb6892896d1951e96b435d'

users=[
	{
		"username" : "testing",
		"password" : "testingpass",
		"email" : "testing@gmail.com"
	}
] 


def checkkey(name):
    try:
        name=request.form[f'{name}']
        return 1
    except:
        return 0

@app.route("/")
def index():
   return render_template('index.html',title="Index")

@app.route("/home")
def home():
   return render_template('home.html',title="Home")


@app.route("/about")
def about():
	return render_template('about.html',title="About")



@app.route("/favicon.ico")
def readme():
	resp=Response(open('static/images/logo.png','rb').read())
	resp.headers['Content-Type']="image/png; charset=utf-8"
	return resp


@app.route("/README.md")
def readme():
	resp=Response(open('README.md','r').read())
	resp.headers['Content-Type']="text/plain; charset=utf-8"
	return resp

@app.route('/register',methods=['GET','POST'])
def register():
	form=RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))
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




@app.route("/signin")
def signin():
	return render_template('login.html',title="Login")

@app.route("/signup")
def signup():
	return render_template('register.html',title="Register")






# Server configuration
if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000,use_reloader=True,debug=True)