from app.service.dtos.admin_dtos import User


class Commuter(User):
    """Used for login"""

    def __init__(self, email, password):
        super().__init__(email, password)


class CommuterFullInfo(Commuter):
    """Used for registration"""
    PHONE_NUMBER_REGEX = r"^\d{10}$"

    def __init__(self, name, password, address, email, tel, dateOfBirth):
        super().__init__(email, password)
        self.name = name
        self.date_of_birth = dateOfBirth
        self.address = address
        self.tel = tel

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "tel": self.tel,
            "dateOfBirth": self.date_of_birth
        }


if __name__ == '__main__':
    commuter = CommuterFullInfo("name", "password", "address", "email@email.com", "tel", "dateOfBirth").to_json()
    print(commuter)
