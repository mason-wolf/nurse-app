import json
from flask import Blueprint, request
from services import auth_service

auth_controller = Blueprint('auth_controller', __name__)

@auth_controller.route("/login", methods=['POST'])
def login():
    credentials = json.loads(request.data)
    return auth_service.login(credentials)