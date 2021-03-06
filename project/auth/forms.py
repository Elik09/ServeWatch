from flask_wtf import FlaskForm
import email_validator as Email
from wtforms import StringField,PasswordField,SubmitField,BooleanField,EmailField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from project.models import User

class RegistrationForm(FlaskForm):
	fname=StringField('First Name',
		validators=[DataRequired(),Length(min=2,max=20)])

	lname=StringField('Last Name',
		validators=[DataRequired(),Length(min=2,max=20)])

	username=StringField('Username',
		validators=[DataRequired(),Length(min=2,max=20)])
	
	phone=StringField('Phone',
		validators=[DataRequired(),Length(min=2,max=14)])

	email=EmailField('Email',
		validators=[DataRequired()])

	password=PasswordField('Password',
		validators=[DataRequired()])

	confirm_password=PasswordField('Confirm Password',
		validators=[DataRequired(),EqualTo('password')])

	submit=SubmitField('Sign Up')

	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken')

	def validate_email(self,email):
		email=User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('That email is taken')

class LoginForm(FlaskForm):
	email=StringField('Email',
		validators=[DataRequired()])

	password=PasswordField('Password',
		validators=[DataRequired()])

	remember=BooleanField('Remember Me')

	submit=SubmitField('Login')