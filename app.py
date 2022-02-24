from flask import Flask

app=Flask(__name__)


if (__name__ == "__main__"):
	# Remember to change this to enviromental variables
	HOST="127.0.0.1"
	PORT=4444
	app.run(debug=True,host=HOST,port=PORT)