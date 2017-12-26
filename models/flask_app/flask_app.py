from flask import Flask
from flask_compress import Compress
from flask_restful import Api, Resource

flask_app = Flask(__name__)
api = Api(flask_app)
Compress(flask_app)
