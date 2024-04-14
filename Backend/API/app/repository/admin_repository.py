from typing import Any

from pymysql import IntegrityError

from app.service.dtos.admin_dtos import Admin, Access, AdminFullInfo
from app.service.dtos.commuter_dtos import SearchAccessQuery
from app.service.exceptions import *


class AdminRepository:

    def __init__(self, database):
        self.database = database

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

    def create_new_access(self, access: Access) -> Access:
        return self.database.create_access(access)

    def get_acess_by_accessId(self, accessId: str) -> Access:
        try:
            access = self.database.get_access(accessId)
            return access
        except KeyError:
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)

    def search_created_access(self, search: SearchAccessQuery):
        return self.database.search_access(search)

    def get_admin_full_info(self, email: str) -> AdminFullInfo:
        admin_info = self.database.fetch_admin_full_info(email)
        if admin_info:
            return admin_info
        else:
            raise InvalidAdmin(ErrorResponseStatus.NOT_FOUND, RequestErrorCause.NOT_FOUND,
                               RequestErrorDescription.NOT_FOUND_DESCRIPTION)
