from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
   return "Hellodfsdf fsdsfadfdafdWorld"


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000,use_reloader=True,debug=True)