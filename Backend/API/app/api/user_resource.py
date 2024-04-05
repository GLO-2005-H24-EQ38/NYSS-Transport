from flask import Flask, request, jsonify

from app.repository.commuter_repository import CommuterRepository
from app.service.commuter_service import CommuterService
from app.service.dtos.admin_dtos import User, Token
from app.service.dtos.commuter_dtos import CommuterFullInfo, Commuter
from app.service.exceptions import RequestError, ErrorResponseStatus

app = Flask(__name__)

# creates a repo by default. if you want to use a different repository, pass it
# as an argument to the CommuterService constructor CommuterService(your_repo)
commuter_service = CommuterService()


@app.route("/user/signup", methods=["POST"])
def signup():
    try:
        data = request.get_json()
        commuter = CommuterFullInfo(**data)
        response = commuter_service.signup_commuter(commuter)
        return jsonify(response)

    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response
    except TypeError as error:
        response = jsonify({"error": str(error)})
        response.status_code = ErrorResponseStatus.BAD_REQUEST.value
        return response


@app.route("/user/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        commuter = Commuter(**data)
        response = commuter_service.login(commuter)
        return jsonify(response.to_json())

    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response
    except TypeError as error:
        response = jsonify({"error": str(error)})
        response.status_code = ErrorResponseStatus.BAD_REQUEST.value
        return response
