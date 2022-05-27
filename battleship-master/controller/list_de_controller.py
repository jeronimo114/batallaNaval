from service.list_de_service import ListDEService
from flask import json, Response,jsonify,Blueprint,request
from util.util_encoder import UtilEncoder
from model.ship import Ship
from service.user_service import UserService

app_user = Blueprint("app_user",__name__)

user_service= UserService()

app_list_de = Blueprint("app_list_de",__name__)
list_de_service = ListDEService()

@app_list_de.route("/list_de")
def list():
    return Response(status=200,mimetype="application/json",
                    response=json.dumps(list_de_service.list(),cls=UtilEncoder))

@app_list_de.route('/listde',methods=['POST'])
def create():
    data = request.json
    return list_de_service.add(Ship(data,list_de_service.list_de.count +1))