import re
import uuid
from datetime import datetime, date

from app.service.dtos.admin_dtos import User, Access
from app.service.exceptions import *
from app.service.exceptions import RequestError, ErrorResponseStatus, RequestErrorCause, RequestErrorDescription


class Commuter(User):
    """Represents a commuter user, used for login"""

    def __init__(self, email, password):
        # Initialize a commuter with email and password
        super().__init__(email, password)


class CommuterFullInfo(Commuter):
    """Represents a commuter user with full information, used for registration"""

    # Regular expressions for phone number and date format validation
    PHONE_NUMBER_REGEX = r"^\d{10}$"
    DATE_REGEX = r"^\d{4}-\d{2}-\d{2}$"

    def __init__(self, name, password, address, email, tel, dateOfBirth):
        # Initialize commuter with full information including name, address, etc.
        super().__init__(email, password)
        self.__check_missing_fields(name, address, tel, dateOfBirth)
        self.__validate_date_of_birth(dateOfBirth)
        self.__validate_phone_number(tel)
        self.name = name
        self.date_of_birth = dateOfBirth
        self.address = address
        self.tel = int(tel)

    def __check_missing_fields(self, name, address, tel, dateOfBirth):
        # Check if all required fields are provided
        if not all(s for s in (name, address, tel, dateOfBirth)):
            raise TypeError("All information fields must be non-empty: name, address, tel, dateOfBirth")

    def __validate_date_of_birth(self, date_of_birth):
        # Validate the format of date of birth and ensure the user is at least 13 years old
        if not date_of_birth:
            raise TypeError("Date of birth is required : dateOfBirth")
        elif not re.match(CommuterFullInfo.DATE_REGEX, date_of_birth):
            raise RequestError(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION, "dateOfBirth")
        else:
            birth_date = datetime.strptime(date_of_birth, '%Y-%m-%d')
            current_today = date.today()
            age = current_today.year - birth_date.year - ((current_today.month, current_today.day) < (birth_date.month, birth_date.day))
            if age < 13:
                raise RequestError(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                   RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION, "dateOfBirth")

    def __validate_phone_number(self, tel):
        # Validate the format of phone number
        if not tel:
            raise TypeError("Phone number is required : tel")
        elif not re.match(CommuterFullInfo.PHONE_NUMBER_REGEX, tel):
            raise RequestError(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION, "tel")

    def to_json(self):
        # Convert commuter object to JSON format
        return {
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "tel": self.tel,
            "dateOfBirth": self.date_of_birth
        }


class CreditCard():
    """Represents a credit card"""
    def __init__(self, holder, expirationDate, cardNumber=None, last4_card_digits=None):
        # Initialize credit card with holder name, expiration date, and optionally card number
        self.holder = self.__validate_holder(holder)
        self.cardNumber = self.__validate_cardNumber(cardNumber)
        self.expirationDate = self.__validate_cardExpirationDate(expirationDate)
        self.last4_card_digits = last4_card_digits

    def __validate_holder(self, holder):
        # Validate the holder name
        if not holder and not holder.strip():
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)
        return holder

    def __validate_cardNumber(self, cardNumber):
        # Validate the format of the card number
        if not (8 <= len(str(cardNumber)) <= 16):
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)
        return cardNumber

    def __validate_cardExpirationDate(self, expirationDate):
        # Validate the expiration date of the card
        exp_date = datetime.strptime(expirationDate, "%m/%y")
        if exp_date <= datetime.now():
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)
        return expirationDate

    def to_json(self):
        # Convert credit card object to JSON format
        return {
            "cardNumber": self.last4_card_digits if self.last4_card_digits else self.cardNumber,
            "holder": self.holder,
            "expirationDate": self.expirationDate,
        }


class Transaction():
    """Represents a transaction"""
    def __init__(self, accessId, quantity):
        # Initialize a transaction with access ID and quantity
        self.accessId = accessId
        self.quantity = self.__validate_quantity(int(quantity))

    def __validate_quantity(self, quantity):
        # Validate the quantity of items in the transaction
        if not (0 < quantity):
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)
        return quantity


class BoughtAccess():
    """Represents an access bought by a commuter"""
    def __init__(self, name, price, accessType, company, accessNumber, expirationDate,
                 transactionDate, transactionNumber, numberOfPassage=None,
                 outOfSale=False, deletionDate=None):
        # Initialize bought access details
        self.accessNumber = accessNumber
        self.price = float(price)
        self.accessName = name
        self.accessType = accessType
        self.transactionDate = transactionDate
        self.expirationDate = expirationDate
        self.transactionNumber = transactionNumber
        self.company = company
        self.numberOfPassage = numberOfPassage
        self.outOfSale = outOfSale
        self.outOfSaleDate = deletionDate

    def to_json(self):
        # Convert bought access object to JSON format
        access_json = {
            "accessNumber": self.accessNumber,
            "price": self.price,
            "accessName": self.accessName,
            "accessType": self.accessType,
            "transactionDate": self.transactionDate,
            "expirationDate": self.expirationDate,
            "transactionNumber": self.transactionNumber,
            "company": self.company,
            "outOfSale": self.outOfSale,
        }
        if self.numberOfPassage is not None:
            access_json["numberOfPassage"] = self.numberOfPassage
        if self.outOfSale:
            access_json["deletionDate"] = self.outOfSaleDate
        return access_json


class SearchAccessQuery():
    """Represents a query to search for access"""
    def __init__(self, name: str = None, accessType: str = None, company: str = None, price: float = None):
        # Initialize search query parameters
        self.accessName = name
        self.accessType = accessType
        self.company = company
        self.price = price

    def searchQuery(self):
        """Fuzzy search for access in the database.
        Search mode are accessName, accessType, company, price"""

        query = ("SELECT access.*, ticket.passes  FROM access LEFT JOIN ticket ON access.id = ticket.access"
                 " WHERE NOT EXISTS(SELECT 1 FROM suspendedAccess s WHERE s.access = access.id)")

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
    """Generates a list of bought accesses"""
    transaction_number = uuid.uuid4().hex  # Generate a single transaction number
    bought_access_list = []
    for _ in range(quantity):
        bought_access = BoughtAccess(access, expiration_date, transaction_number)
        bought_access_list.append(bought_access)
    return bought_access_list
