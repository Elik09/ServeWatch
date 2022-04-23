from . import api
from flask import request
from project import ma 
from project.schema import PostSchema
from project.models import User, LogPost
from project import db
from flask import jsonify
from datetime import datetime

# Sending emails part
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

log_schema = PostSchema()


# Configuration
sender_address = 'servewatch@gmail.com'
sender_pass = 'Servewatch2022!'

# Enter the emails to send to separated with a space
receiver_addresses = 'plexeric40@gmail.com tempmailctf@gmail.com'
receiver_addresses=receiver_addresses.split(' ')
mail_notifications="Enabled"


def sendmessage(subject,mail_content):
    global receiver_addresses,sender_address,sender_pass
    if mail_notifications != "Enabled":
        return False
    for receiver_address in receiver_addresses:
        print(f"[+] Sending email to {receiver_address}")
        try:
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            if len(subject) > 2 :
                message['Subject'] = f'{subject}'   #The subject line
            else:
                message['Subject'] = 'ServeWatch Notification'   #The subject line

            if len(mail_content) < 2:
                mail_content = "Hello,\nFile change detected on server. Please login to check activity.\nThank You"

            #The body and the attachments for the mail
            message.attach(MIMEText(mail_content, 'plain'))
            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            try:
                session.login(sender_address, sender_pass) #login with mail_id and password
            except :
                print("[-] An error occurred while logging in.Make sure the credentials are correct and check this page https://myaccount.google.com/lesssecureapps")
                return False

            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            print(f'[+] Mail Sent to {receiver_address}')
        except Exception as e :
            print(f'[+] Email not sent to {receiver_address} {e}')
            return False
    return True


@api.route('/submit/logs', methods = ['POST'])
def submit_logs():

    log_data = request.get_json(force=True)
   

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
    log.nmapresults  = log_data['nmapresults']

    log.ip = str(request.remote_addr)
    log.modified = datetime.strptime(log_data['timestamp'], '%y%m%d%H%M%S')

    # Sending the email to alert the owner
    # syntax => sendmessage(Subject,Message)
    if 'File_Created' in log.action:
        pass
    else:
        message=f"Hello,\nWe have detected a '{log.action}' activity for file '{log.file_path}' on server {log.machine} with ip {log.ip}. Please login to check activity.\nThank You"
        # print(message)
        try:
            sendmessage("Security Alert",message)
        except:
            print(f"[-] Sending email failed")
            
    db.session.add(log)
    db.session.commit()


    return jsonify({"Message":"Ok"}), 200


    