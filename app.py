#!/usr/bin/env python3

import os

from flask import Flask, jsonify, request, make_response
from flask_restful import Resource
from models import Product, User
from config import db, api, app

print('Hello World')

class Hello(Resource):
    def get(self):
        print('hello world')
api.add_resource(Hello, '/')

