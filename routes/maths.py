from flask import Blueprint, Response, request
from utils.maths import least_common_multiple

maths_blueprint = Blueprint("maths_blueprint", __name__)


@maths_blueprint.route("/math/sum", methods=["GET"])
def next_number():
    number = int(request.args.get("number"))
    return Response(content_type="text/plain", response=f"{number + 1}")


@maths_blueprint.route("/math/mcm", methods=["GET"])
def mcm():
    numbers = request.args.getlist("numbers")
    return Response(
        content_type="text/plain", response=f"{least_common_multiple(numbers)}"
    )
