from datetime import datetime
from platform import machine
from project import ma
from marshmallow import Schema , fields , validates, ValidationError
from project.models import User, Role


class PostSchema(ma.Schema):

    id = fields.String(required = True)
    user = fields.String(required = True)
    machine = fields.String(required=True)
    action = fields.String(required=True)
    file = fields.String(required=True)
    timestamp = fields.String(required = True)


    @validates('timestamp')
    def validate_timestamp(self, timestamp):
        
        try:
            datetime.strptime(timestamp, "%y%m%d%H%M%S")
        except ValueError as error:

            raise ValidationError(error)


class UserShema(ma.Schema):

    oldusername = fields.String(required=True)
    username = fields.String(required=True)
    email = fields.String(required=True)
    role = fields.String(required = False)
    password = fields.String(required = False)
    status = fields.String(required = False)
    ip = fields.String(required=True)

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = None


    @validates('oldusername')
    def validate_oldusername(self, oldusername):

        user = User.query.filter_by(username = oldusername).first()

        if user is None:

            raise ValidationError("No record Found")

        self.user = user


    @validates('username')
    def validate_username(self, username):

        if self.user.username != username and User.query.filter_by(username = username).first():

            raise ValidationError("username is aready registered")


    @validates('email')
    def validates_email(self, email):

        if self.user.email !=email and User.query.filter_by(email = email):

            raise ValidationError("email aready registered")

    @validates('role')
    def validate_role(self, role):

        saved_role = Role.query.filter_by(name = role).first()

        if saved_role is None:

            raise ValidationError("unkown role")


    @validates('status')
    def validate_status(self, status):

        allowed_status = ["active", "suspended"]

        if status not in allowed_status:

            raise ValidationError("unkown status")

    