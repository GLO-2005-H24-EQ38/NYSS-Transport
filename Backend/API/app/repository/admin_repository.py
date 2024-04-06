from app.service.dtos.admin_dtos import Admin, Access
from app.service.exceptions import *


class AdminRepository:

    def __init__(self, database=None):
        dummy_admin = Admin("ema@fd.fasdf", "password", "adminCode")
        dummy_admin.secure_password()
        dummy_admin.secure_admin_code()
        print(dummy_admin)

        self.database = {
            "ema@fd.fasdf": dummy_admin
        }  # TODO will be replaced by the true params of the DB
        self._access = {
            "dummy_access_id": Access(accessName="Dummy Access", price=10.0, accessType="Ticket", duration=4,
                                      company="Dummy Company", numberOfPassage=3)
        }  # TODO will be replaced by the true params of the DB

    def get_created_access(self):
        """this method will be removed when the database is implemented"""
        return self._access

    def get_admin_by_email(self, email: str) -> bool:
        return self.database.get(email)

    def save_access(self, access: Access):
        # TODO review si on doit faire une vérification pour s'assurer
        #  que l'access m'est pas dans la DB déjà
        self._access[access.id] = access

    def get_acess_by_accessId(self, accessId: str) -> Access:
        try:
            access = self._access[accessId]
            return access
        except KeyError:
            raise InvalidCommuter(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                  RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)
