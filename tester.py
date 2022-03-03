#! /usr/bin/python3

from project import db
from project.models import User,Post



db.drop_all()
db.create_all()

userone=User(username="allan",email="allan@gmail.com",password="hackerone")


db.session.add(userone)
db.session.commit()




print(userone)
User.query.all()
