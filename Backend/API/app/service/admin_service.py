from typing import List

from app.service.dtos.admin_dtos import User, Token, AdminFullInfo
from app.service.dtos.admin_dtos import Admin, Access
from app.service.dtos.commuter_dtos import SearchAccessQuery

from app.service.exceptions import *

from app.repository.admin_repository import AdminRepository
from app.service.exceptions import InvalidAdmin


class AdminService():

    def __init__(self, admin_repository: AdminRepository):
        self._admin_repository = admin_repository
        self.logged_in_admin = {}

    def signup_admin(self, new_admin: AdminFullInfo) -> str:
        new_admin.secure_password()
        new_admin.secure_admin_code()
        if self._admin_repository.signup_admin(new_admin):
            return "register successful"
        else:
            raise InvalidCommuter(ErrorResponseStatus.CONFLICT, RequestErrorCause.ALREADY_EXISTS,
                                  RequestErrorDescription.ALREADY_EXISTS_DESCRIPTION)

    def login_admin(self, admin: Admin) -> Token:
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
        # Vérifier si l'utilisateur est authentifié en tant qu'admin
        if token.value not in self.logged_in_admin:
            raise InvalidAdmin(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                               RequestErrorDescription.UNAUTHORIZED_DESCRIPTION)

        if new_access.type not in ["Ticket", "Subscription"]:
            raise InvalidAdmin(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)

        if new_access.type == "Ticket":
            if new_access.numberOfPassage is None:
                raise InvalidAdmin(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.MISSING_PARAMETER,
                                   RequestErrorDescription.MISSING_PARAMETER_DESCRIPTION)
        else:
            # Si ce n'est pas un "Ticket", vérifie que numberOfPassage n'est pas défini
            if new_access.numberOfPassage is not None:
                print(new_access.numberOfPassage)
                raise InvalidAdmin(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                   RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)

        # Stocker l'accès dans la base de données
        self._admin_repository.save_access(new_access)

        # Retourner l'accès créé
        return new_access

    def search_created_access(self, search: SearchAccessQuery) -> List[Access]:
        return self._admin_repository.search_created_access(search)
