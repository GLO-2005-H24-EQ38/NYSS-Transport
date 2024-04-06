from flask import Flask, request, jsonify

from app.repository.admin_repository import AdminRepository
from app.repository.commuter_repository import CommuterRepository
from app.service.commuter_service import CommuterService
from app.service.dtos.admin_dtos import User, Token
from app.service.dtos.commuter_dtos import CommuterFullInfo, Commuter, CreditCard, Transaction
from app.service.dtos.admin_dtos import Admin, Access
from app.service.exceptions import RequestError, ErrorResponseStatus

from app.service.admin_service import AdminService

app = Flask(__name__)

admin_repository = AdminRepository()
commuter_repository = CommuterRepository(
    admin_repository.get_created_access())  # This won't be needed when the database is implemented
commuter_service = CommuterService(commuter_repository, admin_repository)

CREATED = 201
admin_service = AdminService()


@app.route("/user/signup", methods=["POST"])
def signup():
    try:
        data = request.get_json()
        commuter = CommuterFullInfo(**data)
        message = commuter_service.signup_commuter(commuter)
        reponse = jsonify(message)
        reponse.status_code = CREATED
        return reponse

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

@app.route("/user/access/checkout", methods=["GET"])
def buy_access():
    try:
        token = request.headers.get("Authorization")
        cvc = request.headers.get("cvc")
        data = request.get_json()
        transaction = Transaction(**data)
        response = commuter_service.buy_access(Token(token), cvc, transaction)
        # Assuming buy_access returns a list of BoughtAccess objects
        bought_access_json = [bought_access.to_json() for bought_access in response]
        return jsonify(bought_access_json), 200
    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response
    except TypeError as error:
        response = jsonify({"error": str(error)})
        response.status_code = ErrorResponseStatus.BAD_REQUEST.value
        return response