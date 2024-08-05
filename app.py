#!/usr/bin/env python3

import os

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource


app = Flask(__name__)
app.json.compact = False

print('Hello World')

api = Api(app)

class Hello(Resource):
    def get(self):
        print('hello world')
        return 'Hello World'

api.add_resource(Hello, '/')



