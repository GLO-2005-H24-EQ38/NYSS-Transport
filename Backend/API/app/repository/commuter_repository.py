from app.service.dtos.commuter_dtos import Commuter


class CommuterRepository:
    def __init__(self, database):
        self.database = database

    def get_commuter_info(self, email) -> Commuter:
        print('getting info for commuter :', email)
        fake_db_response = {
            "name": "John Doe",
            "email": "yann@me.com",
            "address": "1234 Main St",
            "tel": "1234567890",
            "dateOfBirth": "01/01/2000"         # dd/MM/YYYY
        }
        return Commuter(**fake_db_response)

    def register_commuter(self, commuter: Commuter) -> bool:
        print('registering commuter :', commuter.email)
        return True
