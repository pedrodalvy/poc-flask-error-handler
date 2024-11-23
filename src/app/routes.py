from typing import Dict

from flask import Blueprint

bp = Blueprint("app", __name__, url_prefix="/")


@bp.route("/ping")
def ping() -> Dict[str, str]:
    return {"message": "pong"}
