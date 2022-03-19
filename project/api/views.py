from . import api
from flask import request
from project import ma 
from project.schema import PostSchema
from project.models import User, LogPost
from project import db

from flask import jsonify

from datetime import datetime

log_schema = PostSchema()

@api.route('/submit/logs', methods = ['POST'])
def submit_logs():

    log_data = request.get_json(force=True)
    print(log_data)


    if not log_data:

        return jsonify({"Message":"No Log data passed"}), 400

    validate_errors = log_schema.validate(log_data)

    if validate_errors:

        return jsonify({'Error':F'{validate_errors}'}), 400
 

    log = LogPost()

    log.log_id = log_data['id']
    log.machine = log_data['machine']
    log.user = log_data['user']
    log.action = log_data['action']
    log.file_path  = log_data['file']
    log.ip = request.remote_addr
    log.modified = datetime.strptime(log_data['timestamp'], '%y%m%d%H%M%S')

    db.session.add(log)
    db.session.commit()


    return jsonify({"Message":"Ok"}), 200


    