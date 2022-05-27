from flask import json, Response,jsonify, Blueprint, request
from util.util_encoder import UtilEncoder
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from service.user_service import UserService


app_user= Blueprint("app_user",__name__)
user_service=UserService()

@app_user.route("/user")
@jwt_required()
def get_users():
    return Response(status=200,mimetype="application/json",
                    response=json.dumps(user_service.get_users(),cls=UtilEncoder))

@app_user.route("/user/login", methods=["POST"])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        user = user_service.login(email, password)
        acces_token = create_access_token(identity={'user': user})
        return jsonify({'token':acces_token})
    except Exception as e:
        return jsonify({'message':str(e)})
