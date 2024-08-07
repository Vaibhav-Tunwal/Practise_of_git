from flask import session, request
from flask_restful import Resource,reqparse
from flask_jwt_extended import create_access_token
from models import *
import datetime
class Signin(Resource):
    def post(self):
        loginparser = reqparse.RequestParser()
        loginparser.add_argument('email', type=str)
        loginparser.add_argument('password', type=str)
        args = loginparser.parse_args()

        if args['email'] and args['password']:
            user = User.query.filter_by(email=args['email'],password=args['password']).first()

            if user :
                access_token = create_access_token(identity=user.email, expires_delta=datetime.timedelta(minutes=240) )
                return {"email":user.email ,"access_token":access_token, "role":user.role}, 200
            else :
                
                return {'message' : 'user not found '}, 404
        else :
            return {'message' : 'username and password are required'}, 404
        


class Signup(Resource):
    def post(self):

        try:
            signUpParser = reqparse.RequestParser()
            signUpParser.add_argument('username', type=str)
            signUpParser.add_argument('password', type=str)
            signUpParser.add_argument('role', type=str)
            signUpParser.add_argument('email', type=str)
            args = signUpParser.parse_args()
            user = User(username=args['username'],password=args['password'], email=args['email'], role=args['role'])
            db.session.add(user)

            return {'message': 'signup successful'}, 200
        except:
            db.session.rollback()
            return {'message':'username already exists'}, 400
        finally:
            db.session.commit()
