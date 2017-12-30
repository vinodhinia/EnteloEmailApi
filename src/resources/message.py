import flask
from flask import request
from flask_restful import Resource,reqparse

class MessageResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('to',
                        required = True,
                        help = "This field cannot be blank")
    parser.add_argument('subject',
                        required=True,
                        help="This field cannot be blank")
    parser.add_argument('body',
                        required=True,
                        help="This field cannot be blank")

    def post(self):
        pass

