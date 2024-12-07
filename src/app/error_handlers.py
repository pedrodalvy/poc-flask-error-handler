"""
Error handlers for the app
"""
from http import HTTPStatus
from typing import Tuple

from flask import current_app

from src.app.exceptions import ApplicationError


def handle_exceptions(e: Exception) -> Tuple[dict, int]:
    """
    Handles exceptions raised by the application.

    If the exception is an `ApplicationError`, it is converted to a JSON
    response with the error message and the given status code.

    If the exception is not an `ApplicationError`, it is treated as an
    internal server error, logged to the application logger, and a JSON
    response with the message "Internal Server Error" is returned with the
    status code 500.

    :param e: The exception that was raised
    :return: A tuple of (response, status_code)
    """
    if isinstance(e, ApplicationError):
        return {"message": e.description}, e.code

    current_app.logger.error(f"Unhandled exception: {e}")
    return {"message": "Internal Server Error"}, HTTPStatus.INTERNAL_SERVER_ERROR
