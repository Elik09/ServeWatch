from project import db,login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model,UserMixin):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(20),unique=True,nullable=False)
	password=db.Column(db.String(60),nullable=False)
	email=db.Column(db.String(120),unique=True,nullable=False)
	status=db.Column(db.String(10),nullable=False,default="active")
	role=db.Column(db.String(10),nullable=False,default="viewer")
	created_at=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
	last_login=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
	ip=db.Column(db.String(30),nullable=False,default="127.0.0.1")
	image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
	posts=db.relationship('Post',backref='author',lazy=True)

	def __repr__(self):
		# return f"User('{self.username}','{self.email}','{self.image_file}')"
		string=f"User('{self.id}','{self.username}','{self.password}','{self.email}','{self.status}','{self.role}','{self.created_at}','{self.last_login}','{self.ip}','{self.image_file}','{self.posts}'"
		return string

class Post(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(100),nullable=False)
	date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
	content=db.Column(db.Text,nullable=False)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

	def __repr__(self):
		return f"User('{self.title}','{self.date_posted}')"
