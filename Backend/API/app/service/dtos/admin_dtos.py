import re
import uuid

import bcrypt


class Token():
    """used for user authentication"""

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


class User():
    """Base class for all users (includes admin and commuter)"""

    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    def __init__(self, email, password):
        self.__validate_email(email)
        self.email = email
        self.password = password

    def __validate_email(self, email):
        if not email:
            raise ValueError("Email is required")
        elif not re.match(User.EMAIL_REGEX, email):
            raise ValueError("Invalid email")

    def _hash_secret(self, secret) -> bytes:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(secret.encode(), salt)
        return hashed_password

    def secure_password(self):
        self.password = self._hash_secret(self.password)

    def verify_password(self, password) -> bool:
        return bcrypt.checkpw(password.encode(), self.password)


class Admin(User):

    def __init__(self, email, password, adminCode):
        super().__init__(email, password)
        self.admin_code = adminCode

    def secure_admin_code(self):
        self.admin_code = self._hash_secret(self.admin_code)

    def verify_admin_code(self, admin_code) -> bool:
        return bcrypt.checkpw(admin_code.encode(), self.admin_code)


if __name__ == '__main__':
    admin = Admin("ema@fd.fasdf", "password", "adminCode")

    print(admin.password, admin.admin_code)
    admin.secure_password()
    admin.secure_admin_code()
    print(admin.password, admin.admin_code)
