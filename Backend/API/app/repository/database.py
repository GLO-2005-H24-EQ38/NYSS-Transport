import datetime
import json
import os
from decimal import Decimal
from typing import List

import pymysql
from dotenv import load_dotenv

from app.service.dtos.admin_dtos import Admin, AdminFullInfo, Access
from app.service.dtos.commuter_dtos import Commuter, CommuterFullInfo, CreditCard, SearchAccessQuery
from app.service.exceptions import InvalidCommuter, RequestErrorDescription, RequestErrorCause, ErrorResponseStatus, \
    InvalidAdmin


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
        request = f"CALL RegisterCommuter(%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(request, (
            commuter.email, commuter.name, commuter.password, commuter.address, commuter.date_of_birth, commuter.tel))

        return True

    def fetch_commuter(self, email: str) -> Commuter:
        request = "SELECT email, password FROM user WHERE email = %s"
        self.cursor.execute(request, (email,))
        result = self.cursor.fetchall()

        if result:
            return Commuter(result[0][0], result[0][1])
        else:
            raise InvalidCommuter(ErrorResponseStatus.NOT_FOUND, RequestErrorCause.NOT_FOUND,
                                  RequestErrorDescription.NOT_FOUND_DESCRIPTION)

    def register_admin(self, admin: AdminFullInfo) -> bool:
        request = f"CALL RegisterAdmin(%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(request, (
            admin.email, admin.name, admin.password, admin.address, admin.date_of_birth, admin.tel,
            admin.admin_code, admin.company))

        return True

    def fetch_admin(self, email: str) -> Admin:
        request = "SELECT email, password, code FROM user JOIN admin WHERE email = %s AND user = email"
        self.cursor.execute(request, (email,))
        result = self.cursor.fetchall()

        if result:
            return Admin(result[0][0], result[0][1], result[0][2])
        else:
            raise InvalidAdmin(ErrorResponseStatus.NOT_FOUND, RequestErrorCause.NOT_FOUND,
                               RequestErrorDescription.NOT_FOUND_DESCRIPTION)

    def add_payment_method(self, email: str, credit_card: CreditCard) -> bool:
        request = f"CALL addCreditcard(%s, %s, %s, %s)"
        self.cursor.execute(request, (credit_card.holder, credit_card.cardNumber, credit_card.expirationDate, email))

        return True

    def delete_payment_method(self, email: str) -> bool:
        request = f"CALL deleteCreditcard(%s)"
        self.cursor.execute(request, email)
        return True

    def get_card_info(self, email: str) -> CreditCard | None:
        request = "SELECT GetCreditCard(%s);"
        self.cursor.execute(request, email)
        result = self.cursor.fetchall()

        if result:
            result = json.loads(result[0][0])
            last4_card_digits = result["cardNumber"][:1] + result["cardNumber"][-4:]
            return CreditCard(last4_card_digits=last4_card_digits, **result)
        else:
            return None

    def search_access(self, search: SearchAccessQuery):
        request, parameters = search.searchQuery()

        self.cursor.execute(request, parameters)
        result = self.cursor.fetchall()

        access_list = []
        for access in result:
            access_list.append(Access(
                accesId=access[0],
                accessName=access[1],
                price=access[2],
                company=access[3],
                accessType=access[4],
                duration=access[5],
                numberOfPassage=access[6] if access[4] == "ticket" else None
            ))

        return access_list

    def get_commuter_full_info(self, email: str) -> CommuterFullInfo | None:
        request = "SELECT * FROM user WHERE email = %s and role = 'commuter'"
        self.cursor.execute(request, email)
        result = self.cursor.fetchall()

        if result:
            print(result)
            print(result[0][4].strftime("%Y-%m-%d"))
            commuter = CommuterFullInfo(
                email=result[0][0],
                name=result[0][1],
                password=result[0][2],
                address=result[0][3],
                dateOfBirth=result[0][4].strftime("%Y-%m-%d"),
                tel=str(result[0][5])
            )
            return commuter
        else:
            return None

    def fetch_admin_full_info(self, email: str) -> AdminFullInfo | None:
        request = "SELECT email, name, password, address, birthday, phone, code, company FROM user JOIN admin WHERE email = %s AND user = email"
        self.cursor.execute(request, email)
        result = self.cursor.fetchall()

        if result:
            admin = AdminFullInfo(
                email=result[0][0],
                name=result[0][1],
                password=result[0][2],
                address=result[0][3],
                dateOfBirth=result[0][4].strftime("%Y-%m-%d"),
                tel=str(result[0][5]),
                adminCode=str(result[0][6]),
                company=result[0][7]
            )
            return admin
        else:
            return None

    def close(self):
        self.cursor.close()
        self.connection.close()
        print("Database connection closed")

    def create_access(self, access: Access) -> Access:
        request = "SELECT AddAccess(%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(request, (
            access.id, access.name, access.price, access.company, access.type, access.duration, access.numberOfPassage))
        result = self.cursor.fetchall()
        print("the result: ", result)
        if result:
            result = json.loads(result[0][0])
            print(result)
            return Access(
                accesId=result["accessId"],
                accessName=result["accessName"],
                price=result["price"],
                accessType=result["accessType"],
                duration=result["duration"],
                company=result["company"],
                numberOfPassage=result["numberOfPassage"] if result["accessType"] == "ticket" else None
            )
        else:
            raise InvalidAdmin(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)


if __name__ == '__main__':
    num = str(Decimal('1234567890'))
    print(num)
