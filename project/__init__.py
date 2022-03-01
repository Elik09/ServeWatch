from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# Setting a secret key
app.config['SECRET_KEY'] = 'bed2a11b4ddb6892896d1951e96b435d'
# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
login_manager=LoginManager(app)

from project import routes