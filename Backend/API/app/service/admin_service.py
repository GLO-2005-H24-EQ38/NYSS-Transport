from app.service.dtos.admin_dtos import User, Token
from app.service.dtos.admin_dtos import Admin, Access

from app.service.exceptions import *

from app.repository.admin_repository import AdminRepository
from app.service.exceptions import InvalidAdmin


class AdminService():

    def __init__(self, admin_repository: AdminRepository = AdminRepository()):
        self.admin_repository = admin_repository
        self.logged_in_admin = {}

    def login_admin(self, admin: Admin) -> Token:
        print(admin.email, admin.password, admin.admin_code)
        admin_saved_info = self.admin_repository.get_admin_by_email(admin.email)

        if admin_saved_info.verify_password(admin.password) and admin_saved_info.verify_admin_code(admin.admin_code):
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


        # Générer un identifiant unique pour l'accès
        new_access.secure_access_id()

        # Stocker l'accès dans la base de données
        self.admin_repository.save_access(new_access)

        # Retourner l'accès créé
        return new_access
