from flask_wtf import FlaskForm
import email_validator as Email
from wtforms import StringField,PasswordField,SubmitField,BooleanField,EmailField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from project.models import User


class LogEditForm(FlaskForm):

    pass

class UserEditForm(FlaskForm):

    pass 

