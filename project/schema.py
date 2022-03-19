from datetime import datetime
from project import ma
from marshmallow import Schema , fields , validates, ValidationError
from project.models import User


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
