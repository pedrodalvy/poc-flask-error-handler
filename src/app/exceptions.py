"""
Contais application exceptions
"""
from http import HTTPStatus

from werkzeug.exceptions import HTTPException


class ApplicationError(HTTPException):
    code: int
    description: str


class NotFoundException(ApplicationError):
    code = HTTPStatus.NOT_FOUND
    description = "Not Found"
