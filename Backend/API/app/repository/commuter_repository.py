from typing import List, Any

from pymysql import IntegrityError

from app.repository.database import Database
from app.service.dtos.admin_dtos import Access
from app.service.dtos.commuter_dtos import Commuter, CommuterFullInfo, CreditCard, BoughtAccess, SearchAccessQuery, \
    Transaction
from app.service.exceptions import ErrorResponseStatus, RequestErrorCause, RequestErrorDescription, InvalidCommuter


class CommuterRepository:
    def __init__(self, database: Database, access: dict = {}):

        self.database = database
        self.access = access

    def signup_commuter(self, new_commuter: CommuterFullInfo) -> bool:
        """
        Add a new commuter to the database.
        """
        try:
            return self.database.register_commuter(new_commuter)
        except IntegrityError:
            return False

    def get_commuter_info(self, email: str) -> Any:
        """
        Retrieve commuter information based on email.
        """
        commuter_data = self.database.fetch_commuter(email)
        if commuter_data:
            return commuter_data
        else:
            return None

    def add_payment_method(self, email, credit_card: CreditCard) -> bool:
        """
        Add or update payment method for the commuter with the given email.
        """
        try:
            return self.database.add_payment_method(email, credit_card)
        except IntegrityError:
            return False

    def get_payment_info(self, email) -> CreditCard | None:
        payment_info = self.database.get_card_info(email)
        if payment_info:
            return payment_info
        else:
            raise InvalidCommuter(ErrorResponseStatus.NOT_FOUND, RequestErrorCause.NOT_FOUND,
                                  RequestErrorDescription.NOT_FOUND_DESCRIPTION)

    def buy_access(self, email, transaction: Transaction) -> List[BoughtAccess]:
        return self.database.buy_access(email, transaction)

    def get_bought_access(self, email) -> List[BoughtAccess]:
        commuter_data = self.database.get(email)
        return commuter_data['bought_access']

    def search_access(self, search: SearchAccessQuery) -> List[Access]:
        return self.database.search_access(search)

    def delete_payment_method(self, email) -> bool:
        """
        Add or update payment method for the commuter with the given email.
        """
        try:
            return self.database.delete_payment_method(email)
        except IntegrityError:
            return False

    def get_commuter_full_info(self, email) -> CommuterFullInfo:
        commuter_info = self.database.get_commuter_full_info(email)
        if commuter_info:
            return commuter_info
        else:
            raise InvalidCommuter(ErrorResponseStatus.NOT_FOUND, RequestErrorCause.NOT_FOUND,
                                  RequestErrorDescription.NOT_FOUND_DESCRIPTION)

    def get_acess_by_accessId(self, accessId: str) -> Access:
        access = self.database.get_access(accessId)
        if access:
            return access
        else:
            raise InvalidCommuter(ErrorResponseStatus.NOT_FOUND, RequestErrorCause.NOT_FOUND,
                                  RequestErrorDescription.NOT_FOUND_DESCRIPTION)
