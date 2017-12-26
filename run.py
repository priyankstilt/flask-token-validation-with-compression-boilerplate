from flask_restful import Resource
from models.authentication.v1.token_validation import HTTP_BASIC_AUTH
from models.flask_app.flask_app import flask_app, api

class HelloController(Resource):
    @HTTP_BASIC_AUTH.login_required
    def get(self):
        return {"response" : "hello get"} 


api.add_resource(HelloController, '/api/hello')

if __name__ == '__main__':
    flask_app.run(debug=True)
