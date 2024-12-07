from http.client import HTTPException
from typing import Dict

from flask import Blueprint, request

from src.app.exceptions import NotFoundException

bp = Blueprint("app", __name__, url_prefix="/")


@bp.route("/ping")
def ping() -> Dict[str, str]:
    action = request.args.get('action', 'ok')

    match action:
        case 'ok':
            return {"message": "pong"}
        case 'not_found':
            raise NotFoundException('Not Found')
        case 'not_handled':
            raise HTTPException('Not Handled Error')
