import re
from datetime import datetime

from app.service.dtos.admin_dtos import User
from app.service.exceptions import *


class Commuter(User):
    """Used for login"""

    def __init__(self, email, password):
        super().__init__(email, password)


class CommuterFullInfo(Commuter):
    """Used for registration"""
    PHONE_NUMBER_REGEX = r"^\d{10}$"

    def __init__(self, name, password, address, email, tel, dateOfBirth):
        super().__init__(email, password)
        self.__validate_phone_number(tel)
        self.name = name
        self.date_of_birth = dateOfBirth
        self.address = address
        self.tel = tel

    def __validate_phone_number(self, tel):
        if not tel:
            raise ValueError("Phone number is required")
        elif not re.match(CommuterFullInfo.PHONE_NUMBER_REGEX, tel):
            raise ValueError("Invalid phone number")

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "tel": self.tel,
            "dateOfBirth": self.date_of_birth
        }

class CreditCard():
    def __init__(self, holder, cardNumber, expirationDate):
        self.holder = holder
        self.cardNumber = self.__validate_cardNumber(cardNumber)
        self.expirationDate = self.__validate_cardExpirationDate(expirationDate)

    def __validate_cardNumber(self, cardNumber):
        if not (8 <= len(str(cardNumber)) <= 16):
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER, RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)
        return cardNumber

    def __validate_cardExpirationDate(self, expirationDate):
        exp_date = datetime.strptime(expirationDate, "%m/%y")
        if exp_date <= datetime.now():
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER, RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)
        return expirationDate



if __name__ == '__main__':
    commuter = CommuterFullInfo("name", "password", "address", "email@email.com", "tel", "dateOfBirth").to_json()
    print(commuter)
