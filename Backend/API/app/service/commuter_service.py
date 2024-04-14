from datetime import datetime, timedelta
from typing import List

from app.repository.commuter_repository import CommuterRepository
from app.repository.admin_repository import AdminRepository
from app.service.dtos.admin_dtos import User, Token, Access
from app.service.dtos.commuter_dtos import Commuter, CommuterFullInfo, CreditCard, Transaction, BoughtAccess, \
    generate_bought_access_list, SearchAccessQuery
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

        bought_access_list = self._commuter_repository.buy_access(email, transaction)

        return bought_access_list

    def get_wallet(self, token: Token) -> List[BoughtAccess]:
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

        email = self._logged_in_commuter[token.value]
        wallet = self._commuter_repository.get_bought_access(email)

        return wallet

    def delete_payment_method(self, token: Token) -> str:
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

        email = self._logged_in_commuter[token.value]
        success = self._commuter_repository.delete_payment_method(email)

        if success:
            return "Successfully removed payment method"
        else:
            raise InvalidCommuter(ErrorResponseStatus.NOT_FOUND, RequestErrorCause.NOT_FOUND,
                                  RequestErrorDescription.NOT_FOUND_DESCRIPTION)

    def search_access(self, search: SearchAccessQuery, token: Token) -> List[Access]:
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)
        return self._commuter_repository.search_access(search)

    def get_card_info(self, token: Token) -> CreditCard:
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

        email = self._logged_in_commuter[token.value]
        card_info = self._commuter_repository.get_payment_info(email)

        return card_info

    def get_commuter_full_info(self, token: Token) -> CommuterFullInfo:
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

        email = self._logged_in_commuter[token.value]
        user_info = self._commuter_repository.get_commuter_full_info(email)

        return user_info

    def is_commuter_logged_in(self, token: Token) -> bool:
        return token.value in self._logged_in_commuter
