from app.repository.commuter_repository import CommuterRepository
from app.service.dtos.admin_dtos import User, Token
from app.service.dtos.commuter_dtos import Commuter
from app.service.exceptions import *


class CommuterService():

    def __init__(self, commuter_repository: CommuterRepository = CommuterRepository()):
        self.commuter_repository = commuter_repository
        self.logged_in_commuter = {}

    def signup_commuter(self, new_commuter: Commuter) -> str:
        new_commuter.secure_password()
        if self.commuter_repository.signup_commuter(new_commuter):
            return "register successful"
        else:
            raise InvalidCommuter(ErrorResponseStatus.CONFLICT, RequestErrorCause.ALREADY_EXISTS,
                                  ResquestErrorDescription.ALREADY_EXISTS_DESCRIPTION)

    def login(self, commuter: User) -> Token:
        commuter_saved_info = self.commuter_repository.get_commuter_info(commuter.email)

        if commuter_saved_info.password == commuter.password:
            self.logged_in_commuter = commuter_saved_info
            token = Token()
            self.logged_in_commuter[token.value] = commuter.email
            return token
        else:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  ResquestErrorDescription.UNAUTHORIZED_DESCRIPTION)
