from app.service.dtos.commuter_dtos import Commuter


class CommuterRepository:
    def __init__(self, database=None):
        self.database = {}  # will be replaced with param database but for now it's a dictionary

    def signup_commuter(self, new_commuter: Commuter) -> bool:
        if not self.database.get(new_commuter.email):
            self.database[new_commuter.email] = new_commuter
            return True
        else:
            return False

    def get_commuter_info(self, email) -> Commuter:
        saved_commuter = self.database.get(email)
        return Commuter(**saved_commuter)
