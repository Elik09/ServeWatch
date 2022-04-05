import os

from flask_script import Shell, Manager
from flask_migrate import Migrate, MigrateCommand


#import the app instance from the main blueprint
from project import create_app, db
from project.models import User, LogPost, Role

app = create_app(os.environ.get('ENV_CONFIG') or "default")

manager = Manager(app)
migrate = Migrate(app, db)


##application initalization


#database shell context

def db_shell_context():

    return dict(User = User, Role = Role, Logs = LogPost, db = db)



# application deploy context manager
@manager.command
def deploy():

    

    pass


@manager.command
def setAdmin():

    admin_user = User()
    admin_user.email = os.environ.get('ADMIN_EMAIL')
    admin_user.username = os.environ.get('ADMIN_USERNAME')
    admin_user.password = os.environ.get('ADMIN_PASS')

    db.session.add(admin_user)
    db.session.commit()


@manager.command
def setTestUser():

    testUser = User()
    testUser.email = os.environ.get('TEST_EMAIL')
    testUser.username = os.environ.get('TEST_USERNAME')
    testUser.password = os.environ.get('TEST_PASSWORD')

    db.session.add(testUser)
    db.session.commit()


#register db shell context

manager.add_command("shell", Shell(make_context = db_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ =="__main__":

    manager.run()
