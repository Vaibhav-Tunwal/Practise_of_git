from flask_restful import Api
from flask import Flask
import os
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig
from resources.auth import Signup,Signin
from resources.user import UserResource
from resources.sponsor import SponsorProfileResource
from models import *

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)


    return app

app = create_app()
# celery_app = celery_init_app(app)
CORS(app)

app.app_context().push()
jwt = JWTManager(app)


api = Api(app)
api.add_resource(Signin,'/api/signin')
api.add_resource(Signup,'/api/signup')
api.add_resource(UserResource, '/api/user/<int:user_id>/profile')
api.add_resource(SponsorProfileResource, '/profile/<int:user_id>')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)