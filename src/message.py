import flask
from flask import request
from flask_restful import Resource,reqparse
import smtplib
from email.mime.text import MIMEText

class MessageResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('to',
                        required = True,
                        help = "This field cannot be blank")
    parser.add_argument('subject',
                        required=True,
                        help="This field cannot be blank")
    parser.add_argument('message',
                        required=True,
                        help="This field cannot be blank")

    def post(self):
        #import pdb;pdb.set_trace()
        data = MessageResource.parser.parse_args()
        to = data['to']
        subject = data['subject']
        message = data['message']
        self. create_message('vinuashok29@gmail.com', to, subject, message)

    def create_message(self, sender, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        s = smtplib.SMTP('localhost')
        s.send_message(message)
        s.quit()

