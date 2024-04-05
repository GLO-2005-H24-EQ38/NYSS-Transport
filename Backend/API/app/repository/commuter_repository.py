from app.service.dtos.commuter_dtos import Commuter, CommuterFullInfo


class CommuterRepository:
    def __init__(self, database=None):
        self.database = {}  # will be replaced with param database but for now it's a dictionary

    def signup_commuter(self, new_commuter: Commuter) -> bool:
        if not self.database.get(new_commuter.email):
            self.database[new_commuter.email] = new_commuter
            return True
        else:
            return False

    def get_commuter_info(self, email: str) -> CommuterFullInfo:
        return self.database.get(email)
