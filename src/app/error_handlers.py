from http import HTTPStatus
from typing import Tuple, Dict

from flask import current_app

from src.app.exceptions import ApplicationError


def handle_application_exceptions(error: Exception) -> Tuple[Dict, int]:
    """
    Handles application-wide exception routing with standardized error responses.

    Args:
        error: Exception raised during request processing

    Returns:
        Tuple containing error response and appropriate HTTP status code
    """
    if isinstance(error, ApplicationError):
        return {"message": error.description}, error.code

    current_app.logger.error(f"Unhandled exception: {error}")
    return {"message": "Internal Server Error"}, HTTPStatus.INTERNAL_SERVER_ERROR
