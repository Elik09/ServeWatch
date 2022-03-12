from functools import wraps
from flask import abort
from flask_login import current_user

from .models import Permissions

def permission_required(permission):

    def decorator(function):

        @wraps(function)
        def checker(*args, **kwargs):

            if not current_user.can(permission):

                abort(403)

            return function(*args , **kwargs)

        return checker

    return decorator


def admin_required(function):

    return permission_required(Permissions.ADMINISTRATOR)(function)


