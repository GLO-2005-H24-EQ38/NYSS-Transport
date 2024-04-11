import os
import pymysql
from dotenv import load_dotenv

from app.service.dtos.admin_dtos import Admin, AdminFullInfo
from app.service.dtos.commuter_dtos import Commuter, CommuterFullInfo


class Database:

    def __init__(self):
        """
            Chargez les variables d'environnement de votre fichier .env, puis complétez les lignes 15 à 19 afin de récupérer les valeurs de ces variables
        """
        load_dotenv()
        self.host = os.environ.get("HOST")
        self.port = int(os.environ.get("PORT"))
        self.database = os.environ.get("DATABASE")
        self.user = os.environ.get("USER")
        self.password = os.environ.get("PASSWORD")

        self._open_sql_connection()
        print("Database connection established")

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Database, cls).__new__(cls)
        return cls.instance

    def _open_sql_connection(self):
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.database,
            autocommit=True
        )

        self.cursor = self.connection.cursor()

    def register_commuter(self, commuter: CommuterFullInfo) -> bool:
        request = f"CALL RegisterUser(%s, %s, %s, %s, %s, %s,%s,%s,%s)"
        self.cursor.execute(request, (
            commuter.email, commuter.name, commuter.password, commuter.address, commuter.date_of_birth, commuter.tel,
            "commuter", 0,
            None))

        return True

    def fetch_commuter(self, email: str):
        request = "SELECT email, password FROM user WHERE email = %s"
        self.cursor.execute(request, (email,))
        result = self.cursor.fetchall()
        commuter = Commuter(result[0][0], result[0][1])
        return commuter

    def register_admin(self, admin: AdminFullInfo) -> bool:
        request = f"CALL RegisterUser(%s, %s, %s, %s, %s, %s,%s,%s,%s)"
        self.cursor.execute(request, (
            admin.email, admin.name, admin.password, admin.address, admin.date_of_birth, admin.tel, "admin",
            admin.admin_code, admin.company))

        return True

    def fetch_admin(self, admin: Admin):
        pass
