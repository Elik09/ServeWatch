from flask import Flask,render_template

array="my name is allan njuguna".split(' ')

# Main route
@app.route("/")
@app.route("/home")
def index():
	return "This idsafdfs tfdasfdfhe main page"
	# return render_template('index.html',title="Main Page")

@app.route('/say_hello')
def sayhello(): 
    return "Hello There"

@app.route('/say_hello/<username>')
def sayhellotosomeone(username):
    return f"Hello {username}"

if (__name__ == "__main__"):
    app.run(debug=True)