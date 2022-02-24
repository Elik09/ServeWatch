from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
   return "Hellodfsdf World"


if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)