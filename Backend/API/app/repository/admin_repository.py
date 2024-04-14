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
        Add a new admin.
        """
        try:
            return self.database.register_admin(new_admin)
        except IntegrityError:
            return False

    def get_admin_info(self, email: str) -> Any:
        """
        Retrieve admin information based on email.
        """
        admin = self.database.fetch_admin(email)
        if admin:
            return admin
        else:
            return None

    def create_new_access(self, access: Access) -> Access:
        """
        Create new access based on access details.
        """
        return self.database.admin_create_access(access)

    def search_created_access(self, email: str):
        """
        Create new access based on access details.
        """
        return self.database.admin_search_access(email)

    def get_admin_full_info(self, email: str) -> AdminFullInfo:
        """
        Retrieve all the information of admin based on email.
        """
        admin_info = self.database.fetch_admin_full_info(email)
        if admin_info:
            return admin_info
        else:
            raise InvalidAdmin(ErrorResponseStatus.NOT_FOUND, RequestErrorCause.NOT_FOUND,
                               RequestErrorDescription.NOT_FOUND_DESCRIPTION)

    def suspend_access(self, access_id: str):
        """
        Suspend access based on its id.
        """
        self.database.admin_suspend_access(access_id)
