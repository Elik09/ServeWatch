from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
import email_validator as Email
from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegistrationForm(FlaskForm):
	fname=StringField('First Name',
		validators=[DataRequired(),Length(min=2,max=20)])

	lname=StringField('Last Name',
		validators=[DataRequired(),Length(min=2,max=20)])

	username=StringField('Username',
		validators=[DataRequired(),Length(min=2,max=20)])
	
	phone=StringField('Phone',
		validators=[DataRequired(),Length(min=2,max=14)])

	email=StringField('Email',
		validators=[DataRequired(),Email()])

	password=PasswordField('Password',
		validators=[DataRequired()])

	confirm_password=PasswordField('Confirm Password',
		validators=[DataRequired(),EqualTo('password')])

	submit=SubmitField('Sign Up')


class LoginForm(FlaskForm):
	email=StringField('Email',
		validators=[DataRequired()])

	password=PasswordField('Password',
		validators=[DataRequired()])

	remember=BooleanField('Remember Me')

	submit=SubmitField('Login')