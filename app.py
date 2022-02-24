from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
   return render_template()



@app.route("/about")
def about():
	return "This is the about page"




if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000,use_reloader=True,debug=True)