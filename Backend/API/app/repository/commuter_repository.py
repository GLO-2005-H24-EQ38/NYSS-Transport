from app.service.dtos.commuter_dtos import Commuter, CommuterFullInfo, CreditCard


class CommuterRepository:
    def __init__(self, database=None):
        self.database = {}  # will be replaced with param database but for now it's a dictionary

    def signup_commuter(self, new_commuter: Commuter) -> bool:
        """
        Add a new commuter to the database.
        """
        if not self.database.get(new_commuter.email):
            # Crée un dictionnaire pour stocker le Commuter et les informations de carte de crédit associées
            self.database[new_commuter.email] = {'commuter': new_commuter, 'credit_card': None}
            return True
        else:
            return False

    def get_commuter_info(self, email: str) -> CommuterFullInfo:
        """
        Retrieve commuter information based on email.
        """
        commuter_data = self.database.get(email)
        if commuter_data:
            return commuter_data['commuter']
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