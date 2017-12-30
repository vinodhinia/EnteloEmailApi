import flask
from flask import request
from validate_email import validate_email
from flask_restful import Resource,reqparse
import sendgrid
import os
from sendgrid.helpers.mail import *

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
        data = MessageResource.parser.parse_args()
        to = data['to']
        subject = data['subject']
        message = data['message']

        is_valid = validate_email(to)
        if is_valid is False:
            return {'message' : 'Invalid recipient email. Please enter a valid email address'},400
        if self.send_message(to, subject, message):
            return {'message': 'Email sent successfully'}
        return {'message' : 'Email sending failed'}

    def send_message(self, to, subject, message):
        '''send email to the recipeient via Sendgrid'''
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("entelotest@gmail.com")
        to_email = Email(to)
        content = Content("text/plain", message)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        return response.status_code == 202




