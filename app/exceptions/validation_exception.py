from sanic import SanicException


class ValidationException(SanicException):
    status_code = 400

    def __init__(self, message=""):
        self.message = message
        self.description = self.__class__.__name__
        super().__init__(self.message)