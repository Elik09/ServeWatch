from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
   return render_template('header.html',title="Index")



@app.route("/about")
def about():
	return render_template('about.html',title="About")

@app.route("/array")
def array():
	myarray="this is a simple array".split(' ')
	return render_template('index.html',title="Index",array=myarray)
	# return "This is the array page"

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000,use_reloader=True,debug=True)