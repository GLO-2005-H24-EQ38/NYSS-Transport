from enum import Enum


class ErrorResponseStatus(Enum):
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409
    PAYMENT_REQUIRED = 402
    UNAUTHORIZED = 401


class RequestErrorCause(Enum):
    INVALID_PARAMETER = "INVALID_PARAMETER"
    MISSING_PARAMETER = "MISSING_PARAMETER"
    NOT_FOUND = "NOT_FOUND"
    ALREADY_EXISTS = "ALREADY_EXISTS"
    PAYMENT_REQUIRED = "PAYMENT_REQUIRED"
    UNAUTHORIZED = "UNAUTHORIZED"


class RequestErrorDescription(Enum):
    INVALID_PARAMETER_DESCRIPTION = "Invalid parameter : "
    MISSING_PARAMETER_DESCRIPTION = "Missing parameter"
    NOT_FOUND_DESCRIPTION = "Not found"
    ALREADY_EXISTS_DESCRIPTION = "Already exists"
    PAYMENT_REQUIRED_DESCRIPTION = "Payment required"
    UNAUTHORIZED_DESCRIPTION = "Unauthorized access"


class RequestError(RuntimeError):
    def __init__(self, error_response_status: ErrorResponseStatus, error_cause: RequestErrorCause,
                 description: RequestErrorDescription, param=""):
        self.error_response_status = error_response_status.value
        self.error_cause = error_cause.value
        self.description = description.value
        self.param = param

    def to_json(self):
        return {
            "error_cause": self.error_cause,
            "description": self.description + self.param
        }


class InvalidCommuter(RequestError):
    def __init__(self, error_response_status: ErrorResponseStatus, error_cause: RequestErrorCause,
                 description: RequestErrorDescription, param=""):
        super().__init__(error_response_status, error_cause, description, param)


class InvalidAdmin(RequestError):
    def __init__(self, error_response_status: ErrorResponseStatus, error_cause: RequestErrorCause,
                 description: RequestErrorDescription, param=""):
        super().__init__(error_response_status, error_cause, description, param)
