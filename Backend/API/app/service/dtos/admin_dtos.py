import re
import uuid
from abc import ABC

import random
from datetime import datetime

import bcrypt

from app.service.exceptions import *


class Token():
    """Used for user authentication"""

    def __init__(self, token=None):
        self.value = uuid.uuid4().hex if token is None else token

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other.value

    def to_json(self):
        return {
            "token": self.value
        }


class User(ABC):
    """Base class for all users (includes admin and commuter)"""

    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    def __init__(self, email, password):
        # Initialize user with email and password
        self.__validate_email(email)
        self.__validate_password(password)
        self.email = email
        self.password = password

    def __validate_email(self, email):
        # Validate email format
        if not email:
            raise TypeError("Email is required : email")
        elif not re.match(User.EMAIL_REGEX, email):
            raise RequestError(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION, "email")

    def __validate_password(self, password):
        # Ensure password is provided
        if not password:
            raise TypeError("Password is required : password")

    def _hash_secret(self, secret) -> bytes:
        # Hash the provided secret
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(secret.encode(), salt)
        return hashed_password

    def secure_password(self):
        # Secure the password by hashing it
        self.password = self._hash_secret(self.password)

    def verify_password(self, password) -> bool:
        # Verify the provided password against the hashed password
        return bcrypt.checkpw(password.encode(), self.password.encode())


class Admin(User):

    def __init__(self, email, password, adminCode):
        # Initialize Admin with email, password, and admin code
        super().__init__(email, password)
        self.admin_code = adminCode

    def secure_admin_code(self):
        # Secure the admin code by hashing it
        self.admin_code = self._hash_secret(self.admin_code)

    def verify_admin_code(self, admin_code) -> bool:
        # Verify the provided admin code against the hashed admin code
        return bcrypt.checkpw(admin_code.encode(), self.admin_code.encode())


class AdminFullInfo(Admin):
    """Used for Admin registration"""
    PHONE_NUMBER_REGEX = r"^\d{10}$"
    DATE_REGEX = r"^\d{4}-\d{2}-\d{2}$"

    def __init__(self, name, password, address, email, tel, dateOfBirth, adminCode, company):
        # Initialize Admin with full information including name, address, etc.
        super().__init__(email, password, adminCode)
        self.__check_missing_fields(name, address, tel, dateOfBirth, company)
        self.__validate_date_of_birth(dateOfBirth)
        self.__validate_phone_number(tel)
        self.name = name
        self.date_of_birth = dateOfBirth
        self.address = address
        self.tel = int(tel)
        self.company = company

    def __check_missing_fields(self, name, address, tel, dateOfBirth, company):
        # Check if all required fields are provided
        if not all(s for s in (name, address, tel, dateOfBirth, company)):
            raise TypeError("All information fields must be non-empty: name, address, tel, dateOfBirth, company")

    def __validate_date_of_birth(self, date_of_birth):
        # Validate the format of date of birth and ensure the user is at least 13 years old
        if not date_of_birth:
            raise TypeError("Date of birth is required : dateOfBirth")
        elif not re.match(AdminFullInfo.DATE_REGEX, date_of_birth):
            raise RequestError(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION, "dateOfBirth")
        else:
            birth_date = datetime.strptime(date_of_birth, '%Y-%m-%d')
            age = (datetime.now() - birth_date).days // 365
            if age < 13:
                raise RequestError(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                   RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION, "dateOfBirth")

    def __validate_phone_number(self, tel):
        # Validate the format of phone number
        if not tel:
            raise TypeError("Phone number is required : tel")
        elif not re.match(AdminFullInfo.PHONE_NUMBER_REGEX, tel):
            raise RequestError(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION, "tel")

    def validate_code(self):
        # Validate the admin code format and checksum
        try:
            # Extract the random string and checksum from the code
            random_string = self.admin_code[:-1]
            provided_checksum = int(self.admin_code[-1])

            # Calculate checksum
            calculated_checksum = sum(ord(char) for char in random_string) % 10

            # Check if the provided checksum matches the calculated checksum
            if provided_checksum != calculated_checksum:
                raise InvalidAdmin(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                   RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION, "adminCode")
        except BaseException:
            raise RequestError(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION, "adminCode")

    def to_json(self):
        # Convert Admin object to JSON format
        return {
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "tel": self.tel,
            "dateOfBirth": self.date_of_birth,
            "company": self.company
        }


class Access:
    TICKET = "ticket"
    SUBSCRIPTION = "subscription"

    def __init__(self, accessName, price, accessType, duration, company, accesId=None, numberOfPassage=None,
                 outOfSale=False, deletionDate=None):
        self.id = uuid.uuid4().hex[:8] if accesId is None else accesId
        self.name = accessName
        self.price = float(price)
        self.type = accessType
        self.duration = int(duration)
        self.company = company
        self.outOfSale = outOfSale
        self.outOfSaleDate = deletionDate
        self.numberOfPassage = int(numberOfPassage) if numberOfPassage is not None else None

    def to_json(self):
        # Convert Access object to JSON format
        access_json = {
            "accessId": self.id,
            "accessName": self.name,
            "price": self.price,
            "accessType": self.type,
            "duration": self.duration,
            "company": self.company,
            "outOfSale": self.outOfSale,
        }
        if self.numberOfPassage is not None:
            access_json["numberOfPassage"] = self.numberOfPassage
        if self.outOfSale:
            access_json["deletionDate"] = self.outOfSaleDate
        return access_json


def generate_code():
    """generate a random code for admin registration, with a checksum at the end.
    this way the only to create an admin is to have the correct code provided by the issuer (NYSS developers)."""

    # Generate a random 5-character alphanumeric string
    random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))

    # Calculate checksum
    checksum = sum(ord(char) for char in random_string) % 10

    # Append checksum to the string
    code = random_string + str(checksum)

    return code