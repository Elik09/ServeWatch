import  os

basedir = os.path.abspath(os.path.dirname(__file__))
from dotenv import load_dotenv

class Config:

    #Load the .env file configs
    load_dotenv()
    #Global Application Config

    SECRET_KEY = os.environ.get('SECRET_KEY');
    MAIL_ADMIN = os.environ.get('ADMIN_EMAIL')

    DEBUG = True

    #Email support configs

    #Database configs

    SQLALCHEMY_COMMITON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    @staticmethod
    def init_app(app):

        pass


class DevelopmentConfig(Config):

    #Development Database config

    SQLALCHEMY_DATABASE_URI  = os.environ.get('DEVELOPMENT_DB_URI') or "sqlite:///" + os.path.join(basedir, 'dev.sqlite3')
    
    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):

    pass


config = {

    'default':DevelopmentConfig,
    'development':DevelopmentConfig,
    'production':ProductionConfig,
}