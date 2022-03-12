from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from flask_login import LoginManager


from config import config


db=SQLAlchemy()
login_manager=LoginManager()
login_manager.session_protection = 'strong'


#app factory method
def create_app(env_config):

    app = Flask(__name__)
    app.config.from_object(config[env_config])
    config[env_config].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)


    #Application Blueprint registration
    from project.auth import auth
    app.register_blueprint(auth)

    from project.main import main
    app.register_blueprint(main)

    #API REGISTRATION 

    from project.api import api
    app.register_blueprint(api)
    
    return app