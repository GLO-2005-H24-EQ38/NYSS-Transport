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
                               ResquestErrorDescription.UNAUTHORIZED_DESCRIPTION)

    def create_access(self, new_access: Access, token: Token) -> Access:
        # Vérifier si l'utilisateur est authentifié en tant qu'admin
        if token.value not in self.logged_in_admin:
            raise InvalidAdmin(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                               ResquestErrorDescription.UNAUTHORIZED_DESCRIPTION)

        # Insérer ici la logique pour vérifier le type d'accès et d'autres critères
        if new_access.type not in ["Ticket", "Subscription"]:
            raise InvalidAdmin(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               ResquestErrorDescription.INVALID_PARAMETER_DESCRIPTION)

        if new_access.type == "Ticket" and not new_access.passes:
            raise InvalidAdmin(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.MISSING_PARAMETER,
                               ResquestErrorDescription.MISSING_PARAMETER_DESCRIPTION)

        # Générer un identifiant unique pour l'accès
        new_access.secure_access_id()

        # Insérez ici la logique pour stocker l'accès dans votre base de données
        self.admin_repository.save_access(new_access)

        # Retourner l'accès créé
        return new_access