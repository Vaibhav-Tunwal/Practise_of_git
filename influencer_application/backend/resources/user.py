from flask import request
from flask_restful import Resource
from models import User, Influencer, db

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        
        user_data = {
            'username': user.username,
            'email': user.email,
            'username': user.username,
            'email': user.email,
        }

        influencer = Influencer.query.filter_by(user_id=user_id).first()
        if influencer:
            user_data.update({
                'name': influencer.name,
                'category': influencer.category,
                'niche': influencer.niche,
                'reach': influencer.reach,
                'rating': influencer.rating,
                'earnings': influencer.earnings
            })

        return user_data, 200

    def post(self, user_id):
        print("hello")
        # data = request.get_json()

        # user = User.query.get(user_id)
        # if not user:
        #     return {'message': 'User not found'}, 404

        # influencer = Influencer.query.filter_by(user_id=user_id).first()
        # if not influencer:
        #     influencer = Influencer(user_id=user_id)

        # influencer.name = data.get('name', influencer.name)
        # influencer.category = data.get('category', influencer.category)
        # influencer.niche = data.get('niche', influencer.niche)
        # influencer.reach = data.get('reach', influencer.reach)
        # influencer.rating = data.get('rating', influencer.rating)
        # influencer.earnings = data.get('earnings', influencer.earnings)

        # db.session.add(influencer)
        # db.session.commit()

        # return {'message': 'Profile updated successfully'}, 200
