from app.repository.commuter_repository import CommuterRepository
from app.service.dtos.admin_dtos import Token
from app.service.dtos.commuter_dtos import Commuter, CommuterFullInfo
from app.service.exceptions import *


class CommuterService():

    def __init__(self, commuter_repository: CommuterRepository):
        self._commuter_repository = commuter_repository
        self._logged_in_commuter = {}

    def signup_commuter(self, new_commuter: CommuterFullInfo) -> str:
        new_commuter.secure_password()
        if self._commuter_repository.signup_commuter(new_commuter):
            return "register successful"
        else:
            raise InvalidCommuter(ErrorResponseStatus.CONFLICT, RequestErrorCause.ALREADY_EXISTS,
                                  ResquestErrorDescription.ALREADY_EXISTS_DESCRIPTION)

    def login(self, commuter: Commuter) -> Token:
        print(commuter.email, commuter.password)
        commuter_saved_info = self._commuter_repository.get_commuter_info(commuter.email)

        if commuter_saved_info.verify_password(commuter.password):
            token = Token()
            self._logged_in_commuter[token.value] = commuter.email
            return token
        else:
            raise InvalidCommuter(ErrorResponseStatus.UNAUTHORIZED, RequestErrorCause.UNAUTHORIZED,
                                  ResquestErrorDescription.UNAUTHORIZED_DESCRIPTION)
