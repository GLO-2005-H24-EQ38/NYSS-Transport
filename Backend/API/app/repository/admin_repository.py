from app.service.dtos.admin_dtos import Admin, Access



class AdminRepository:

    def __init__(self, database=None):
        dummy_admin = Admin("ema@fd.fasdf", "password", "adminCode")
        dummy_admin.secure_password()
        dummy_admin.secure_admin_code()
        print(dummy_admin)

        self.database = {
            "ema@fd.fasdf": dummy_admin
        } #TODO will be replaced by the true params of the DB
        self._access = {}

    def get_created_access(self):
        """this method will be removed when the database is implemented"""
        return self._access

    def get_admin_by_email(self, email: str) -> bool:
        return self.database.get(email)

    def save_access(self, access: Access):
        #TODO review si on doit faire une vérification pour s'assurer
        # que l'acess m'est pas dans la DB déjà
        self.database[access.id] = access

