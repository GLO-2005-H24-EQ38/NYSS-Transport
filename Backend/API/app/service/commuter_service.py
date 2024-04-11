from datetime import datetime, timedelta
from typing import List

from app.repository.commuter_repository import CommuterRepository
from app.repository.admin_repository import AdminRepository
from app.service.dtos.admin_dtos import User, Token
from app.service.dtos.commuter_dtos import Commuter, CommuterFullInfo, CreditCard, Transaction, BoughtAccess, \
    generate_bought_access_list
from app.service.exceptions import *


class CommuterService():

    def __init__(self, commuter_repository: CommuterRepository, admin_repository: AdminRepository):
        self._commuter_repository = commuter_repository
        self._admin_repository = admin_repository
        self._logged_in_commuter = {}

    def signup_commuter(self, new_commuter: CommuterFullInfo) -> str:
        new_commuter.secure_password()
        if self._commuter_repository.signup_commuter(new_commuter):
            return "register successful"
        else:
            raise InvalidCommuter(ErrorResponseStatus.CONFLICT, RequestErrorCause.ALREADY_EXISTS,
                                  RequestErrorDescription.ALREADY_EXISTS_DESCRIPTION)

    def login(self, commuter: Commuter) -> Token:
        print(commuter.email, commuter.password)
        commuter_saved_info = self._commuter_repository.get_commuter_info(commuter.email)

        if commuter_saved_info and commuter_saved_info.verify_password(commuter.password):
            token = Token()
            self._logged_in_commuter[token.value] = commuter.email
            return token
        else:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

    def add_payment_method(self, credit_card: CreditCard, token: Token) -> str:
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

        email = self._logged_in_commuter[token.value]
        success = self._commuter_repository.add_payment_method(email, credit_card)

        if success:
            return "Successfully added payment method"
        else:
            raise InvalidCommuter(ErrorResponseStatus.NOT_FOUND, RequestErrorCause.NOT_FOUND,
                                  RequestErrorDescription.NOT_FOUND_DESCRIPTION)

    def buy_access(self, token: Token, cvc: int, transaction: Transaction) -> List[BoughtAccess]:
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)
        if len(str(cvc)) != 3:
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)

        email = self._logged_in_commuter[token.value]
        if self._commuter_repository.get_payment_method(email) is None:
            raise InvalidCommuter(ErrorResponseStatus.PAYMENT_REQUIRED, RequestErrorCause.PAYMENT_REQUIRED,
                                  RequestErrorDescription.PAYMENT_REQUIRED_DESCRIPTION)

        # TODO 	Est-ce qu'on code ceci: le cvc doit confirmer que la carte de credit est valide avant d'entamer le paiement.

        access = self._admin_repository.get_acess_by_accessId(transaction.accessId)

        duration_days = access.duration
        current_date = datetime.now().date()
        expiration_date = current_date + timedelta(days=duration_days)
        expiration_date_str = expiration_date.strftime("%Y/%m/%d")

        bought_access = generate_bought_access_list(access, expiration_date_str, transaction.quantity)
        self._commuter_repository.add_bought_access(email, bought_access)

        return bought_access

    def get_wallet(self, token: Token) -> List[BoughtAccess]:
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

        email = self._logged_in_commuter[token.value]
        wallet = self._commuter_repository.get_bought_access(email)

        return wallet
