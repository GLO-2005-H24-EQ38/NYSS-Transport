from flask import Flask, request, jsonify

from app.service.commuter_service import CommuterService
from app.service.dtos.admin_dtos import User
from app.service.dtos.commuter_dtos import CommuterFullInfo
from app.service.exceptions import RequestError

app = Flask(__name__)

commuter_service = CommuterService()


@app.route("/user/signup", methods=["POST"])
def signup():
    try:
        data = request.get_json()
        commuter = CommuterFullInfo(**data)
        response = commuter_service.register_commuter(commuter)
        return jsonify(response)
    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response

@app.route("/user/login", methods=["POST"])
def signup():
    try:
        data = request.get_json()
        commuter = User(**data)
        response = commuter_service.login(commuter)
        return jsonify(response)
    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response