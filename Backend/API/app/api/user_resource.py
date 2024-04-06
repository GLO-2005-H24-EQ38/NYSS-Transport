from flask import Flask, request, jsonify

from app.repository.commuter_repository import CommuterRepository
from app.service.commuter_service import CommuterService
from app.service.dtos.admin_dtos import User, Token
from app.service.dtos.commuter_dtos import CommuterFullInfo, Commuter, CreditCard
from app.service.dtos.admin_dtos import Admin, Access
from app.service.exceptions import RequestError, ErrorResponseStatus

from app.service.admin_service import AdminService

app = Flask(__name__)

# creates a repo by default. if you want to use a different repository, pass it
# as an argument to the CommuterService constructor CommuterService(your_repo)
commuter_service = CommuterService()
admin_service = AdminService()


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
        if "adminCode" in data:
            admin = Admin(**data)
            response = admin_service.login_admin(admin)
        else:
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

@app.route("/user/admin/access", methods=["POST"])
def create_access():
    try:
        token = request.headers.get("Authorization")
        data = request.get_json()
        access = Access(**data)
        response = admin_service.create_access(access, Token(token))
        return jsonify(response.to_json()), 201
    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response
    except TypeError as error:
        response = jsonify({"error": str(error)})
        response.status_code = ErrorResponseStatus.BAD_REQUEST.value
        return response

@app.route("/user/payment", methods=["POST"])
def add_payment_method():
    try:
        token = request.headers.get("Authorization")
        data = request.get_json()
        credit_card = CreditCard(**data)
        response = commuter_service.add_payment_method(credit_card, Token(token))
        return jsonify({"message": response}), 201
    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response
    except TypeError as error:
        response = jsonify({"error": str(error)})
        response.status_code = ErrorResponseStatus.BAD_REQUEST.value
        return response