
from flask.json import jsonify
from flask_jwt_extended import create_access_token
from services import user_service
from models.user import User


def login(credentials):
    user = User(credentials["username"], credentials["password"])
    login = user_service.load_user(user.email, user.password)
    if login is not None:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token, 
                       username=user.email, userId=user.id)
    else:
        return {"error": "403"}