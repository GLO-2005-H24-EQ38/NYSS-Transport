from flask import Flask, request, jsonify
from flask_cors import cross_origin

from app.repository.admin_repository import AdminRepository
from app.repository.commuter_repository import CommuterRepository
from app.service.commuter_service import CommuterService
from app.service.dtos.admin_dtos import User, Token, AdminFullInfo
from app.service.dtos.commuter_dtos import CommuterFullInfo, Commuter, CreditCard, Transaction, SearchAccessQuery
from app.service.dtos.admin_dtos import Admin, Access
from app.service.exceptions import RequestError, ErrorResponseStatus

from app.service.admin_service import AdminService
from app.repository.database import Database

database = Database()
app = Flask(__name__)

admin_repository = AdminRepository(database=database)
admin_service = AdminService(admin_repository)

commuter_repository = CommuterRepository(database=database)
commuter_service = CommuterService(commuter_repository, admin_repository)

CREATED = 201


@app.route("/user/signup", methods=["POST"])
@cross_origin()
def signup():
    try:
        data = request.get_json()
        if "adminCode" in data:
            admin = AdminFullInfo(**data)
            message = admin_service.signup_admin(admin)
        else:
            commuter = CommuterFullInfo(**data)
            message = commuter_service.signup_commuter(commuter)
        response = jsonify(message)
        response.status_code = CREATED
        return response

    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response
    except TypeError as error:
        response = jsonify({"error": str(error)})
        response.status_code = ErrorResponseStatus.BAD_REQUEST.value
        return response


@app.route("/user/login", methods=["POST"])
@cross_origin()
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


@app.route("/admin/access", methods=["POST"])
@cross_origin()
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
@cross_origin()
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


@app.route("/user/access/checkout", methods=["POST"])
@cross_origin()
def buy_access():
    try:
        token = request.headers.get("Authorization")
        cvc = request.headers.get("cvc")
        data = request.get_json()
        transaction = Transaction(**data)

        response = commuter_service.buy_access(Token(token), int(cvc), transaction)
        bought_access_json = [bought_access.to_json() for bought_access in response]

        return jsonify(bought_access_json), 200
    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response
    # except TypeError as error:
    #     response = jsonify({"error": str(error)})
    #     response.status_code = ErrorResponseStatus.BAD_REQUEST.value
    #     return response


@app.route("/user/access", methods=["GET"])
@cross_origin()
def get_wallet():
    try:
        token = request.headers.get("Authorization")
        response = commuter_service.get_wallet(Token(token))

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


@app.route("/user/payment", methods=["DELETE"])
@cross_origin()
def delete_payment_method():
    try:
        token = request.headers.get("Authorization")
        response = commuter_service.delete_payment_method(Token(token))
        return jsonify({"message": response}), 204
    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response
    except TypeError as error:
        response = jsonify({"error": str(error)})
        response.status_code = ErrorResponseStatus.BAD_REQUEST.value
        return response


@app.route("/user/access/search", methods=["POST"])
@cross_origin()
def commuter_access_search():
    try:
        token = request.headers.get("Authorization")
        data = request.get_json()
        search_query = SearchAccessQuery(**data)
        found_access = commuter_service.search_access(search_query, Token(token))

        response = [access.to_json() for access in found_access]

        return jsonify(response), 200
    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response
    except TypeError as error:
        response = jsonify({"error": str(error)})
        response.status_code = ErrorResponseStatus.BAD_REQUEST.value
        return response


@app.route("/admin/access/search", methods=["GET"])
@cross_origin()
def admin_access_search():
    try:
        token = request.headers.get("Authorization")
        found_access = admin_service.search_created_access(Token(token))

        response = [access.to_json() for access in found_access]

        return jsonify(response), 200
    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response
    except TypeError as error:
        response = jsonify({"error": str(error)})
        response.status_code = ErrorResponseStatus.BAD_REQUEST.value
        return response


@app.route("/user/payment", methods=["GET"])
@cross_origin()
def get_card_info():
    try:
        token = request.headers.get("Authorization")
        response = commuter_service.get_card_info(Token(token))
        return jsonify(response.to_json()), 200
    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response
    except TypeError as error:
        response = jsonify({"error": str(error)})
        response.status_code = ErrorResponseStatus.BAD_REQUEST.value
        return response


@app.route("/user", methods=["GET"])
@cross_origin()
def get_commuter():
    try:
        token = request.headers.get("Authorization")
        response = commuter_service.get_commuter_full_info(Token(token))
        return jsonify(response.to_json()), 200
    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response
    except TypeError as error:
        response = jsonify({"error": str(error)})
        response.status_code = ErrorResponseStatus.BAD_REQUEST.value
        return response


@app.route("/admin", methods=["GET"])
@cross_origin()
def get_admin():
    try:
        token = request.headers.get("Authorization")
        response = admin_service.get_admin_full_info(Token(token))
        return jsonify(response.to_json()), 200
    except RequestError as error:
        response = jsonify(error.to_json())
        response.status_code = error.error_response_status
        return response
    except TypeError as error:
        response = jsonify({"error": str(error)})
        response.status_code = ErrorResponseStatus.BAD_REQUEST.value
        return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
