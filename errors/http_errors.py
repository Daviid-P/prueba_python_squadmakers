from http.client import HTTPException
from flask import Blueprint, jsonify

http_errors_blueprint = Blueprint("http_errors_blueprint", __name__)


@http_errors_blueprint.errorhandler(HTTPException)
def handle_404_exception(e):
    return jsonify({"error": "This endpoint doesn't exist."})
