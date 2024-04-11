from typing import List, Any

from pymysql import IntegrityError

from app.repository.database import Database
from app.service.dtos.commuter_dtos import Commuter, CommuterFullInfo, CreditCard, BoughtAccess


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
        commuter_data = self.database.get(email)
        if commuter_data:
            if commuter_data['credit_card'] is None:
                commuter_data['credit_card'] = credit_card
            else:
                print("Replacing existing credit card information")
                commuter_data['credit_card'] = credit_card
            return True
        else:
            return False

    def get_payment_method(self, email) -> str | None:

        commuter_data = self.database.get(email)
        if commuter_data['credit_card'] is None:
            return None
        else:
            return commuter_data['credit_card']

    def add_bought_access(self, email, bought_access: List[BoughtAccess]):
        commuter_data = self.database.get(email)
        if commuter_data:
            commuter_data['bought_access'].extend(bought_access)

    def get_bought_access(self, email) -> List[BoughtAccess]:
        commuter_data = self.database.get(email)
        return commuter_data['bought_access']
