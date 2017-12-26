''' Class to handle the basic authentication token matching '''
from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

class TokenValidator(object):
    ''' Class using basic http authentication of flask to secure the end point '''
    SECRET_KEY = 'This is test'

    @staticmethod
    def generate_auth_object():
        ''' Return the basic authentication object '''
        token_validator = TokenValidator()
        return token_validator

    @staticmethod
    def generate_token():
        ''' Generate authentication token '''
        # This key should be changed to config file based method
        # Second parameter can be expiration at the moment, there is no expiration
        serializer = Serializer(TokenValidator.SECRET_KEY)
        return serializer.dumps({'id': 1}) # Right now its 1 default ID it should be user id

    @staticmethod
    def verify_token(token):
        ''' Verify token passed to the end point '''
        serializer = Serializer(TokenValidator.SECRET_KEY)
        try:
            data = serializer.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        return data

HTTP_BASIC_AUTH = HTTPBasicAuth()

@HTTP_BASIC_AUTH.verify_password
def verify_password(username_or_token, password):
    ''' Verify token passed to the end point, password is useless at the moment '''
    user = TokenValidator.verify_token(username_or_token)
    return user
