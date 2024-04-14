import datetime
import json
import os
from decimal import Decimal
from typing import List

import pymysql
from dotenv import load_dotenv
from pymysql import OperationalError, IntegrityError

from app.service.dtos.admin_dtos import Admin, AdminFullInfo, Access
from app.service.dtos.commuter_dtos import Commuter, CommuterFullInfo, CreditCard, SearchAccessQuery, BoughtAccess
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
        """
            Open SQL connection using pymysql
        """
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
        """
        Register a new commuter in the database.
        """
        request = f"CALL RegisterCommuter(%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(request, (
            commuter.email, commuter.name, commuter.password, commuter.address, commuter.date_of_birth, commuter.tel))

        return True

    def fetch_commuter(self, email: str) -> Commuter:
        """
        Fetch commuter details from the database
        """
        request = "SELECT email, password FROM user WHERE email = %s"
        self.cursor.execute(request, (email,))
        result = self.cursor.fetchall()

        if result:
            return Commuter(result[0][0], result[0][1])
        else:
            raise InvalidCommuter(ErrorResponseStatus.NOT_FOUND, RequestErrorCause.NOT_FOUND,
                                  RequestErrorDescription.NOT_FOUND_DESCRIPTION)

    def register_admin(self, admin: AdminFullInfo) -> bool:
        """
        Register a new admin in the database.
        """
        request = f"CALL RegisterAdmin(%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(request, (
            admin.email, admin.name, admin.password, admin.address, admin.date_of_birth, admin.tel,
            admin.admin_code, admin.company))

        return True

    def fetch_admin(self, email: str) -> Admin:
        """
        Fetch commuter details from the database.
        """
        request = "SELECT email, password, code FROM user JOIN admin WHERE email = %s AND user = email"
        self.cursor.execute(request, (email,))
        result = self.cursor.fetchall()

        if result:
            return Admin(result[0][0], result[0][1], result[0][2])
        else:
            raise InvalidAdmin(ErrorResponseStatus.NOT_FOUND, RequestErrorCause.NOT_FOUND,
                               RequestErrorDescription.NOT_FOUND_DESCRIPTION)

    def add_payment_method(self, email: str, credit_card: CreditCard) -> bool:
        """
        Add a payment method (credit card) for a commuter in the database.
        """
        request = f"CALL addCreditcard(%s, %s, %s, %s)"
        self.cursor.execute(request, (credit_card.holder, credit_card.cardNumber, credit_card.expirationDate, email))
        return True

    def delete_payment_method(self, email: str) -> bool:
        """
        Delete a payment method (credit card) for a commuter in the database.
        """
        request = f"CALL deleteCreditcard(%s)"
        self.cursor.execute(request, email)
        return True

    def get_card_info(self, email: str) -> CreditCard | None:
        """
        Retrieve credit card information of a commuter from the database.
        """
        request = "SELECT GetCreditCard(%s);"
        self.cursor.execute(request, email)
        result = self.cursor.fetchall()
        if result[0][0]:
            result = json.loads(result[0][0])
            last4_card_digits = result["cardNumber"][:1] + result["cardNumber"][-4:]
            return CreditCard(last4_card_digits=last4_card_digits, **result)
        else:
            return None

    def commuter_search_access(self, search: SearchAccessQuery) -> List[Access]:
        """
        Search for access available for a commuter in the database.
        """
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
                numberOfPassage=access[7] if access[4] == "ticket" else None
            ))
        return access_list

    def admin_search_access(self, email: str) -> List[Access]:
        """
        Search for access for an admin in the database.
        """
        request = (
            "SELECT access.*, ticket.passes, suspendedAccess.deletionDate FROM access "
            "LEFT JOIN ticket ON access.id = ticket.access "
            "LEFT JOIN suspendedAccess ON access.id = suspendedAccess.access "
            "WHERE access.company = (SELECT company FROM admin WHERE user = %s)")

        self.cursor.execute(request, email)
        result = self.cursor.fetchall()
        print(result)

        access_list = []
        for access in result:
            access_list.append(Access(
                accesId=access[0],
                accessName=access[1],
                price=access[2],
                company=access[3],
                accessType=access[4],
                duration=access[5],
                outOfSale=True if access[6] else False,
                numberOfPassage=access[7] if access[4] == "ticket" else None,
                deletionDate=access[8].strftime("%Y-%m-%d") if access[6] else None
            ))
        return access_list

    def fetch_commuter_full_info(self, email: str) -> CommuterFullInfo | None:
        """
        Retrieve all the information of a commuter from the database.
        """
        request = "SELECT * FROM user WHERE email = %s and role = 'commuter'"
        self.cursor.execute(request, email)
        result = self.cursor.fetchall()

        if result:
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
        """
        Retrieve all the information of an admin from the database.
        """
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

    def admin_create_access(self, access: Access) -> Access:
        """
        Create new access by admin in the database.
        """
        request = "SELECT AddAccess(%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(request, (
            access.id, access.name, access.price, access.company, access.type, access.duration, access.numberOfPassage))
        result = self.cursor.fetchall()

        if result:
            result = json.loads(result[0][0])
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

    def admin_suspend_access(self, access_id: str):
        """
        Suspend access by admin in the database.
        """
        request = "CALL DeleteAccess(%s)"
        try:
            self.cursor.execute(request, access_id)
        except IntegrityError:
            pass  # ignored request because the Access was already suspended
        except OperationalError as error:
            raise InvalidAdmin(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                               RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION, str(error))

    def buy_access(self, email, transaction) -> List[BoughtAccess]:
        """
        Buy access by commuter in the database.
        """
        try:
            request = "SELECT BuyAccess(%s, %s, %s)"
            self.cursor.execute(request, (transaction.quantity, email, transaction.accessId))
            result = self.cursor.fetchall()

            if result:
                print(result)
                result = json.loads(result[0][0])

                bought_access_list = []
                for access in result:
                    bought_access_list.append(BoughtAccess(
                        accessNumber=access["accessNumber"],
                        price=access["price"],
                        name=access["name"],
                        accessType=access["accessType"],
                        transactionDate=access["transactionDate"],
                        expirationDate=access["expirationDate"],
                        transactionNumber=access["transactionNumber"],
                        company=access["company"],
                        outOfSale=True if access["outOfSale"] else False,
                        deletionDate=access.get("outOfSaleDate") if access[
                                                                        "outOfSale"] is True else None,
                        numberOfPassage=access.get("numberOfPassage") if access["accessType"] == "ticket" else None
                    ))
                return bought_access_list
            else:
                raise InvalidAdmin(ErrorResponseStatus.BAD_REQUEST, RequestErrorCause.INVALID_PARAMETER,
                                   RequestErrorDescription.INVALID_PARAMETER_DESCRIPTION)
        except OperationalError as error:
            raise InvalidAdmin(ErrorResponseStatus.PAYMENT_REQUIRED, RequestErrorCause.PAYMENT_REQUIRED,
                               RequestErrorDescription.PAYMENT_REQUIRED_DESCRIPTION, str(error))

    def fetch_commuter_bought_access(self, email) -> List[BoughtAccess]:
        """
        Retrieve all the access a commuter bought from the database.
        """
        request = "SELECT GetAccessBought(%s);"
        self.cursor.execute(request, email)
        result = self.cursor.fetchall()

        bought_access_list = []

        if result[0][0]:
            result = json.loads(result[0][0].strip("'"))
            for access in result:
                bought_access_list.append(BoughtAccess(
                    accessNumber=access["accessNumber"],
                    price=access["price"],
                    name=access["name"],
                    accessType=access["accessType"],
                    transactionDate=access["transactionDate"],
                    expirationDate=access["expirationDate"],
                    transactionNumber=access["transactionNumber"],
                    company=access["company"],
                    outOfSale=True if access["outOfSale"] else False,
                    deletionDate=access.get("deletionDate") if access["outOfSale"] else None,
                    numberOfPassage=access.get("numberOfPassage") if access["accessType"] == "ticket" else None
                ))
        return bought_access_list

    def fetch_companies_names(self):
        """
        Retrieve all the companies names.
        """
        request = "SELECT name FROM company"
        self.cursor.execute(request)
        result = self.cursor.fetchall()
        companies = []
        for company in result:
            companies.append(company[0])
        return companies

