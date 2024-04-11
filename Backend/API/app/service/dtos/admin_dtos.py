import re
import uuid
from abc import ABC

import bcrypt

from app.service.exceptions import *


class Token():
    """Used for user authentication"""

    def __init__(self, token=uuid.uuid4().hex):
        self.value = token

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
        self.__validate_email(email)
        self.__validate_password(password)
        self.email = email
        self.password = password

    def __validate_email(self, email):
        if not email:
            raise TypeError("Email is required : email")
        elif not re.match(User.EMAIL_REGEX, email):
            raise RequestError(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION, "email")

    def __validate_password(self, password):
        if not password:
            raise TypeError("Password is required : password")

    def _hash_secret(self, secret) -> bytes:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(secret.encode(), salt)
        return hashed_password

    def secure_password(self):
        self.password = self._hash_secret(self.password)

    def verify_password(self, password) -> bool:
        return bcrypt.checkpw(password.encode(), self.password.encode())


class Admin(User):

    def __init__(self, email, password, adminCode):
        super().__init__(email, password)
        self.admin_code = adminCode

    def secure_admin_code(self):
        self.admin_code = self._hash_secret(self.admin_code)

    def verify_admin_code(self, admin_code) -> bool:
        return bcrypt.checkpw(admin_code.encode(), self.admin_code.encode())


class Access:
    def __init__(self, accessName, price, accessType, duration, company, numberOfPassage=None):
        self.id = uuid.uuid4().hex
        self.name = accessName
        self.price = float(price)
        self.type = accessType
        self.duration = int(duration)
        self.company = company
        self.numberOfPassage = int(numberOfPassage) if numberOfPassage is not None else None

    def to_json(self):
        access_json = {
            "accessId": self.id,
            "accessName": self.name,
            "price": self.price,
            "accessType": self.type,
            "duration": self.duration,
            "company": self.company,
        }
        if self.numberOfPassage is not None:
            access_json["numberOfPassage"] = self.numberOfPassage
        return access_json

