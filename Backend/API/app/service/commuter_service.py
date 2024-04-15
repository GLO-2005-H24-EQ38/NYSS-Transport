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
        """
        Initializes the CommuterService with the necessary repositories.
        """
        self._commuter_repository = commuter_repository
        self._admin_repository = admin_repository
        self._logged_in_commuter = {}

    def signup_commuter(self, new_commuter: CommuterFullInfo) -> str:
        """
        Signs up a new commuter and adds them to the system.
        """
        new_commuter.secure_password()
        if self._commuter_repository.signup_commuter(new_commuter):
            return "register successful"
        else:
            raise InvalidCommuter(ErrorResponseStatus.CONFLICT, RequestErrorCause.ALREADY_EXISTS,
                                  RequestErrorDescription.ALREADY_EXISTS_DESCRIPTION)

    def login(self, commuter: Commuter) -> Token:
        """
        Logs in a commuter and generates a token for authentication.
        """
        commuter_saved_info = self._commuter_repository.get_commuter_info(commuter.email)

        if commuter_saved_info and commuter_saved_info.verify_password(commuter.password):
            token = Token()
            self._logged_in_commuter[token.value] = commuter.email
            return token
        else:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

    def add_payment_method(self, credit_card: CreditCard, token: Token) -> str:
        """
        Adds a payment method to a commuter's account.
        """
        # Confirm that the commuter is logged in
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

        # Retrieve the email based on the token
        email = self._logged_in_commuter[token.value]
        success = self._commuter_repository.add_payment_method(email, credit_card)

        if success:
            return "Successfully added payment method"
        else:
            raise InvalidCommuter(ErrorResponseStatus.NOT_FOUND, RequestErrorCause.NOT_FOUND,
                                  RequestErrorDescription.NOT_FOUND_DESCRIPTION)

    def buy_access(self, token: Token, cvc: int, transaction: Transaction) -> List[BoughtAccess]:
        """
        Buys access to a service using a commuter's account.
        """
        # Confirm that the commuter is logged in
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)
        # Confirm that the CVC contains 3 characters
        if len(str(cvc)) != 3:
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)

        # Retrieve the email based on the token
        email = self._logged_in_commuter[token.value]

        bought_access_list = self._commuter_repository.buy_access(email, transaction)

        return bought_access_list

    def get_wallet(self, token: Token) -> List[BoughtAccess]:
        """
        Retrieves the wallet of a commuter, containing bought access instances.
        """
        # Confirm that the commuter is logged in
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)
        # Retrieve the email based on the token
        email = self._logged_in_commuter[token.value]
        wallet = self._commuter_repository.get_bought_access(email)

        return wallet

    def delete_payment_method(self, token: Token):
        """
        Deletes a payment method from a commuter's account.
        """
        # Confirm that the commuter is logged in
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

        # Retrieve the email based on the token
        email = self._logged_in_commuter[token.value]

        success = self._commuter_repository.delete_payment_method(email)

        if not success:
            raise InvalidCommuter(ErrorResponseStatus.NOT_FOUND, RequestErrorCause.NOT_FOUND,
                                  RequestErrorDescription.NOT_FOUND_DESCRIPTION)

    def search_access(self, search: SearchAccessQuery, token: Token) -> List[Access]:
        """
        Searches for access based on the provided query.
        """
        # Confirm that the commuter is logged in
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)
        return self._commuter_repository.search_access(search)

    def get_card_info(self, token: Token) -> CreditCard:
        """
        Retrieves the credit card information associated with a commuter's account.
        """
        # Confirm that the commuter is logged in
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

        # Retrieve the email based on the token
        email = self._logged_in_commuter[token.value]

        card_info = self._commuter_repository.get_payment_info(email)

        return card_info

    def get_commuter_full_info(self, token: Token) -> CommuterFullInfo:
        """
        Retrieves the full information of a commuter.
        """
        # Confirm that the commuter is logged in
        if token.value not in self._logged_in_commuter:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

        # Retrieve the email based on the token
        email = self._logged_in_commuter[token.value]

        user_info = self._commuter_repository.get_commuter_full_info(email)

        return user_info

    def is_commuter_logged_in(self, token: Token) -> bool:
        """
        Confirms if the commuter is logged in.
        """
        return token.value in self._logged_in_commuter

    def logout_commuter(self, token: Token):
        """
        Logs out a commuter.
        """
        if token.value in self._logged_in_commuter:
            del self._logged_in_commuter[token.value]
