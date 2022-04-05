from email.policy import default
from sqlalchemy import Column
from project import db,login_manager
from datetime import datetime
from flask_login import UserMixin, AnonymousUserMixin
from flask import current_app
from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash

from project import db



@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class Permissions:

	CREATEACCOUNT= 0X02
	DELETEACCOUNT= 0X04
	SUSPENDACCOUNT = 0X08
	EDITACCOUNT = 0X10
	VIEWLOGS = 0X20
	SUBMITLOGS =0X40
	EDITLOGS = 0X80
	ADMINISTRATOR = 0XFF


class User(db.Model,UserMixin):

	__tablename__ = "users"

	id=db.Column(db.Integer,primary_key=True)

	username=db.Column(db.String(50),unique=True,nullable=False)

	password_hash=db.Column(db.String(200),nullable=False)

	email=db.Column(db.String(120),unique=True,nullable=False)

	status=db.Column(db.String(50),default="active")

	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	created_at=db.Column(db.DateTime,default=datetime.utcnow)

	last_login=db.Column(db.DateTime,default=datetime.utcnow)

	ip=db.Column(db.String(100),default="127.0.0.1")

	image_file=db.Column(db.String(100),default='default.jpg')


	def __init__(self, **kwargs):

		super(User, self).__init__(**kwargs)

		if self.role is None:

			if self.email == current_app.config['MAIL_ADMIN'] and current_app.config['MAIL_ADMIN'] is not None:

				self.roles = Role.query.filter_by(permissions=0xff).first()

		if self.role is None:

			self.role = Role.query.filter_by(default =True).first()




	# make the password word attribute not accessible via the class object once it is assigned
	@property
	def password(self):

		return AttributeError("Access Denied")

	@password.setter
	def password(self, password):

		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):

		return check_password_hash(self.password_hash, password)

		
	def can(self, permissions):

		#perform a logical AND operation to confirm if a user has the given permissions

		return self.role is not None and (self.role.permissions & permissions) == permissions


	def is_admin(self):

		return self.can(Permissions.ADMINISTRATOR)

	def __repr__(self):
		# return f"User('{self.username}','{self.email}','{self.image_file}')"
		string= f"User({self.username})"
		return string


class Role(db.Model):

	__tablename__ ="roles"

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), nullable = False)
	default = db.Column(db.Boolean, default = False, index = True)

	permissions = db.Column(db.Integer)

	users = db.relationship('User', backref='role', lazy='dynamic')

	@staticmethod
	def register_roles():

		roles = {

			"viewer":(Permissions.SUBMITLOGS | Permissions.VIEWLOGS, True),
			"admin": (0xff, False)
		}

		for r in roles:

			role = Role.query.filter_by(name = r).first()

			if role is None:

				role = Role(name = r)
				role.permissions = roles[r][0]
				role.default = roles[r][1]

				db.session.add(role)


		db.session.commit()


	def __repr__(self) -> str:

		return f"Role({self.name})"


class LogPost(db.Model):
	__tablename__ = "logs"
	id = db.Column(db.Integer, primary_key = True)
	log_id = db.Column(db.String(200), nullable=False)
	user = db.Column(db.String(200), nullable = False)
	machine=db.Column(db.String(100),nullable=False)
	action =db.Column(db.String(100), nullable = False)
	file_path = db.Column(db.String(500))
	ip = db.Column(db.String(500),nullable=False,default="None")
	modified = db.Column(db.DateTime, nullable = False)
	date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

	

	def __repr__(self):
		return f"Post('{self.log_id}','{self.date_posted}')"



class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):

        return False

    def is_admin(self):

        return False

login_manager.anonymous_user = AnonymousUser