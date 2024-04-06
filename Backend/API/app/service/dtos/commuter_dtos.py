import re

from app.service.dtos.admin_dtos import User
from app.service.exceptions import RequestError, ErrorResponseStatus, RequestErrorCause, ResquestErrorDescription


class Commuter(User):
    """Used for login"""

    def __init__(self, email, password):
        super().__init__(email, password)


class CommuterFullInfo(Commuter):
    """Used for registration"""
    PHONE_NUMBER_REGEX = r"^\d{10}$"
    DATE_REGEX = r"^\d{2}/\d{2}/\d{4}$"

    def __init__(self, name, password, address, email, tel, dateOfBirth):
        super().__init__(email, password)
        self.__check_missing_fields(name, address, tel, dateOfBirth)
        self.__validate_date_of_birth(dateOfBirth)
        self.__validate_phone_number(tel)
        self.name = name
        self.date_of_birth = dateOfBirth
        self.address = address
        self.tel = int(tel)

    def __check_missing_fields(self, name, address, tel, dateOfBirth):

        if not all(s for s in (name, address, tel, dateOfBirth)):
            raise TypeError("All information fields must be non-empty: name, address, tel, dateOfBirth")

    def __validate_date_of_birth(self, date_of_birth):
        if not date_of_birth:
            raise TypeError("Date of birth is required : dateOfBirth")
        elif not re.match(CommuterFullInfo.DATE_REGEX, date_of_birth):
            raise RequestError(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               ResquestErrorDescription.INVALID_PARAMETER_DESCRIPTION, "dateOfBirth")

    def __validate_phone_number(self, tel):
        if not tel:
            raise TypeError("Phone number is required : tel")
        elif not re.match(CommuterFullInfo.PHONE_NUMBER_REGEX, tel):
            raise RequestError(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               ResquestErrorDescription.INVALID_PARAMETER_DESCRIPTION, "tel")

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "tel": self.tel,
            "dateOfBirth": self.date_of_birth
        }


if __name__ == '__main__':
    commuter = CommuterFullInfo("name", "password", "address", "email@email.com", "0123456789", "dateOfBirth").to_json()
    print(commuter)
    if ("  ".strip()):
        print("True")
