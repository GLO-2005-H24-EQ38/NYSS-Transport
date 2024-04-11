from typing import Any

from pymysql import IntegrityError

from app.service.dtos.admin_dtos import Admin, Access, AdminFullInfo
from app.service.exceptions import *


class AdminRepository:

    def __init__(self, database):
        self.database = database
        self._access = {
            "dummy_access_id": Access(accessName="Dummy Access", price=10.0, accessType="Ticket", duration=4,
                                      company="Dummy Company", numberOfPassage=3),
            "dummy_access_sub_id": Access(accessName="Dummy Access", price=10.0, accessType="Subscription", duration=4,
                                          company="Dummy Company")
        }

    def signup_admin(self, new_admin: AdminFullInfo) -> bool:
        """
        Add a new commuter to the database.
        """
        try:
            return self.database.register_admin(new_admin)
        except IntegrityError:
            return False

    def get_created_access(self):
        """this method will be removed when the database is implemented"""
        return self._access

    def get_admin_info(self, email: str) -> Any:
        admin = self.database.fetch_admin(email)
        if admin:
            return admin
        else:
            return None

    def save_access(self, access: Access):
        self._access[access.id] = access

    def get_acess_by_accessId(self, accessId: str) -> Access:
        try:
            access = self._access[accessId]
            return access
        except KeyError:
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)
