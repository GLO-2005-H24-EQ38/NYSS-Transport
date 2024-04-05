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


class ResquestErrorDescription(Enum):
    INVALID_PARAMETER_DESCRIPTION = "Invalid parameter"
    MISSING_PARAMETER_DESCRIPTION = "Missing parameter"
    NOT_FOUND_DESCRIPTION = "Not found"
    ALREADY_EXISTS_DESCRIPTION = "Already exists"
    PAYMENT_REQUIRED_DESCRIPTION = "Payment required"
    UNAUTHORIZED_DESCRIPTION = "Unauthorized access"


class RequestError(RuntimeError):
    def __init__(self, error_response_status: ErrorResponseStatus, error_cause: RequestErrorCause,
                 description: ResquestErrorDescription):
        self.error_response_status = error_response_status.value
        self.error_cause = error_cause.value
        self.description = description.value

    def to_json(self):
        return {
            "error_cause": self.error_cause,
            "description": self.description
        }


class InvalidCommuter(RuntimeError):
    def __init__(self, error_response_status: ErrorResponseStatus, error_cause: RequestErrorCause,
                 description: ResquestErrorDescription):
        super().__init__(error_response_status, error_cause, description)


class InvalidAdmin(RuntimeError):
    def __init__(self, error_response_status: ErrorResponseStatus, error_cause: RequestErrorCause,
                 description: ResquestErrorDescription):
        super().__init__(error_response_status, error_cause, description)
