from http.client import HTTPException

from flask import Blueprint, request, jsonify, Response

from src.app.exceptions import NotFoundException

bp = Blueprint("health", __name__, url_prefix="/")


@bp.route("/ping")
def health_check() -> Response:
    """
    Provides a health check endpoint with different response modes.

    Query parameters:
    - action: Determines the response type
        'ok' (default): Returns a success response
        'not_found': Raises a NotFoundException
        'not_handled': Raises an HTTPException
    """
    action = request.args.get('action', 'ok')

    match action:
        case 'ok':
            return jsonify({"message": "pong"})
        case 'not_found':
            raise NotFoundException('Resource not found')
        case 'not_handled':
            raise HTTPException('Unhandled error occurred')
        case _:
            raise ValueError(f'Invalid action: {action}')
