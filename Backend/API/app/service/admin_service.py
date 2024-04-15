from typing import List

from app.service.dtos.admin_dtos import User, Token, AdminFullInfo
from app.service.dtos.admin_dtos import Admin, Access
from app.service.dtos.commuter_dtos import SearchAccessQuery

from app.service.exceptions import *

from app.repository.admin_repository import AdminRepository
from app.service.exceptions import InvalidAdmin


class AdminService():

    def __init__(self, admin_repository: AdminRepository):
        """
        Initializes the AdminService with the necessary repository.
        """
        self._admin_repository = admin_repository
        self.logged_in_admin = {}

    def signup_admin(self, new_admin: AdminFullInfo) -> str:
        """
        Signs up a new admin and adds them to the system.
        """
        new_admin.validate_code()
        new_admin.secure_password()
        new_admin.secure_admin_code()
        if self._admin_repository.signup_admin(new_admin):
            return "register successful"
        else:
            raise InvalidCommuter(ErrorResponseStatus.CONFLICT, RequestErrorCause.ALREADY_EXISTS,
                                  RequestErrorDescription.ALREADY_EXISTS_DESCRIPTION)

    def login_admin(self, admin: Admin) -> Token:
        """
        Logs in an admin and generates a token for authentication.
        """
        admin_saved_info = self._admin_repository.get_admin_info(admin.email)

        if admin_saved_info and admin_saved_info.verify_password(admin.password) and admin_saved_info.verify_admin_code(
                admin.admin_code):
            token = Token()
            self.logged_in_admin[token.value] = admin.email
            return token
        else:
            raise InvalidAdmin(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                               RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

    def create_access(self, new_access: Access, token: Token) -> Access:
        """
        Creates a new access in the system.
        """
        # Confirm that the commuter is logged in
        self.check_user_validity(token)

        # Verify that the access type is only ticket and subscription
        if new_access.type not in ["ticket", "subscription"]:
            raise InvalidAdmin(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)

        # Verify that numberOfPassage is present if it's a ticket
        if new_access.type == "ticket":
            if new_access.numberOfPassage is None:
                raise InvalidAdmin(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.MISSING_PARAMETER,
                                   RequestErrorDescription.MISSING_PARAMETER_DESCRIPTION)
        else:
            # If it's not a ticket, verify that numberOfPassage is not defined
            if new_access.numberOfPassage is not None:
                print(new_access.numberOfPassage)
                raise InvalidAdmin(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                   RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)

        return self._admin_repository.create_new_access(new_access)

    def get_admin_full_info(self, token: Token) -> AdminFullInfo:
        """
        Retrieves the full information of an admin.
        """
        # Confirm that the commuter is logged in
        self.check_user_validity(token)

        # Retrieve the email based on the token
        email = self.logged_in_admin[token.value]

        return self._admin_repository.get_admin_full_info(email)

    def search_created_access(self, token: Token) -> List[Access]:
        """
        Searches all created access from the admin's company.
        """
        # Confirm that the commuter is logged in
        self.check_user_validity(token)

        return self._admin_repository.search_created_access(self.logged_in_admin[token.value])

    def suspend_access(self, access_id: str, token: Token):
        """
        Suspends an access from the company.
        """
        # Confirm that the commuter is logged in
        self.check_user_validity(token)
        self._admin_repository.suspend_access(access_id)
        return "Successfully removed access from sale"

    def check_user_validity(self, token):
        if token.value not in self.logged_in_admin:
            raise InvalidAdmin(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                               RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

    def is_admin_logged_in(self, token: Token) -> bool:
        """
        Confirms if the admin is logged in.
        """
        return token.value in self.logged_in_admin

    def get_companies_names(self):
        """
         Retrieves all the companies.
         """
        return self._admin_repository.get_companies_names()

    def logout_admin(self, token: Token):
        """
        Logs out an admin.
        """
        if token.value in self.logged_in_admin:
            del self.logged_in_admin[token.value]