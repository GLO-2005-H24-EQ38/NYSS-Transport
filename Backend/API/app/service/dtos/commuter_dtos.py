import re
import uuid
from datetime import datetime

from app.service.dtos.admin_dtos import User, Access
from app.service.exceptions import *
from app.service.exceptions import RequestError, ErrorResponseStatus, RequestErrorCause, RequestErrorDescription


class Commuter(User):
    """Used for login"""

    def __init__(self, email, password):
        super().__init__(email, password)


class CommuterFullInfo(Commuter):
    """Used for registration"""
    PHONE_NUMBER_REGEX = r"^\d{10}$"
    DATE_REGEX = r"^\d{4}-\d{2}-\d{2}$"

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
                               RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION, "dateOfBirth")

    def __validate_phone_number(self, tel):
        if not tel:
            raise TypeError("Phone number is required : tel")
        elif not re.match(CommuterFullInfo.PHONE_NUMBER_REGEX, tel):
            raise RequestError(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION, "tel")

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "tel": self.tel,
            "dateOfBirth": self.date_of_birth
        }


class CreditCard():
    def __init__(self, holder, expirationDate, cardNumber=None, last4_card_digits=None):
        self.holder = self.__validate_holder(holder)
        self.cardNumber = self.__validate_cardNumber(cardNumber)
        self.expirationDate = self.__validate_cardExpirationDate(expirationDate)
        self.last4_card_digits = last4_card_digits

    def __validate_holder(self, holder):
        if not holder and not holder.strip():
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)
        return holder

    def __validate_cardNumber(self, cardNumber):
        if not (8 <= len(str(cardNumber)) <= 16):
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)
        return cardNumber

    def __validate_cardExpirationDate(self, expirationDate):
        exp_date = datetime.strptime(expirationDate, "%m/%y")
        if exp_date <= datetime.now():
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)
        return expirationDate

    def to_json(self):
        return {
            "cardNumber": self.last4_card_digits if self.last4_card_digits else self.cardNumber,
            "holder": self.holder,
            "expirationDate": self.expirationDate,
        }


class Transaction():
    def __init__(self, accessId, quantity):
        self.accessId = accessId
        self.quantity = self.__validate_quantity(int(quantity))

    def __validate_quantity(self, quantity):
        if not (0 < quantity):
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)
        return quantity


class BoughtAccess():
    def __init__(self, access: Access, expirationDate: str, transactionNumber: str):
        self.accessNumber = uuid.uuid4().hex
        self.accessName = access.name
        self.accessType = self.__validate_access_type(access.type)
        self.transactionDate = datetime.now().strftime("%Y/%m/%d")
        self.expirationDate = self.__validate_date_format(expirationDate)
        self.transactionNumber = transactionNumber
        self.company = access.company
        self.numberOfPassage = int(access.numberOfPassage) if access.numberOfPassage is not None else None

    def to_json(self):
        print("-----converting into JSON----")
        access_json = {
            "accessNumber": self.accessNumber,
            "accessName": self.accessName,
            "accessType": self.accessType,
            "transactionDate": self.transactionDate,
            "expirationDate": self.expirationDate,
            "transactionNumber": self.transactionNumber,
            "company": self.company,
        }
        if self.numberOfPassage is not None:
            access_json["numberOfPassage"] = self.numberOfPassage
        return access_json

    def __validate_date_format(self, date_string):
        pattern = r"\d{4}/\d{2}/\d{2}"
        if re.match(pattern, date_string):
            return date_string
        else:
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)

    def __validate_access_type(self, access_type):
        if access_type not in ["Ticket", "Subscription"]:
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)
        return access_type


class SearchAccessQuery():
    def __init__(self, name: str = None, accessType: str = None, company: str = None, price: float = None):
        self.accessName = name
        self.accessType = accessType
        self.company = company
        self.price = price

    def searchQuery(self):
        """Fuzzy search for access in the database."""

        query = "SELECT * FROM access WHERE 1=1"

        parameters = []

        if self.accessName:
            query += " AND LOWER(name) LIKE LOWER(%s)"
            parameters.append('%' + ' '.join(map(re.escape, self.accessName.split())) + '%')

        if self.accessType:
            query += " AND LOWER(type) LIKE LOWER(%s)"
            parameters.append('%' + ' '.join(map(re.escape, self.accessType.split())) + '%')

        if self.company:
            query += " AND LOWER(company) LIKE LOWER(%s)"
            parameters.append('%' + ' '.join(map(re.escape, self.company.split())) + '%')

        if self.price:
            query += " AND price <= %s"
            parameters.append(self.price)

        query += ";"

        return query, parameters


def generate_bought_access_list(access, expiration_date, quantity):
    transaction_number = uuid.uuid4().hex  # Generate a single transaction number
    bought_access_list = []
    for _ in range(quantity):
        bought_access = BoughtAccess(access, expiration_date, transaction_number)
        bought_access_list.append(bought_access)
    return bought_access_list
