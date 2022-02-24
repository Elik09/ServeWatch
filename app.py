from flask import Flask,render_template,url_for

app=Flask(__name__)


array="my name is allan njuguna".split(' ')

# Main route
@app.route("/")
@app.route("/home")
def index():
	return render_template('header.html',title="Main Page")

@app.route('/checkme')
def checkme():
	return "this works"
	# return render_template('index.html',array=array)

# Configurations
if (__name__ == "__main__"):
	# Remember to change this to enviromental variables
	HOST="127.0.0.1"
	PORT=5000
	app.run(debug=True,host=HOST,port=PORT)