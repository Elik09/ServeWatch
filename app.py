from flask import Flask,render_template,url_for,Response

app = Flask(__name__)

users=[
	{
		"  username" : "testing",
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


def readfile(filename):
	try:
		with open(filename,"r") as f:
			contents=f.read()
			f.close()
		return contents
	except:
		return "Unable to read the file"

@app.route("/README.md")
def readme():
	resp=open('README.md','r').read()
	resp.headers['Content-Type']="text/plain; charset=utf-8"
	return resp



@app.route("/login")
def login():
	return render_template('login.html',title="Login")

@app.route("/register")
def register():
	return render_template('register.html',title="Register")






# Server configuration
if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000,use_reloader=True,debug=True)