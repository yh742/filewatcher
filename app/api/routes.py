from flask import Blueprint
from flask_restful import Api, Resource

mod = Blueprint('api', __name__)
api = Api(mod)

class Hello(Resource):
    def get(self):
        return {"message": "Hello, World!"}

api.add_resource(Hello, '/Hello')