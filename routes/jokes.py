from random import randint

from flask import Blueprint, Response, abort, jsonify, request
from utils.fake_db import (
    get_chuck_norris_joke,
    get_dad_joke,
    create_joke,
    update_joke,
)
from utils.fake_db import delete_joke as _delete_joke

jokes_blueprint = Blueprint("jokes_blueprint", __name__)


@jokes_blueprint.route("/joke/", methods=["GET"])
def get_random_joke():
    if randint(0, 1):
        return jsonify({"joke": get_chuck_norris_joke()})
    else:
        return jsonify({"joke": get_dad_joke()})


@jokes_blueprint.route("/joke/<string:joke_type>", methods=["GET"])
def get_specific_joke(joke_type: str):
    AVAILABLE_JOKES = {
        "chuck": get_chuck_norris_joke,
        "dad": get_dad_joke,
    }
    try:
        return jsonify({"joke": AVAILABLE_JOKES[joke_type.lower()]()})
    except KeyError as e:
        abort(404)


@jokes_blueprint.route("/joke/", methods=["POST"])
def post_joke():
    data = request.get_json()
    print(data)
    if "the_joke" not in data or data["the_joke"].strip() == "":
        abort(422)
    joke = create_joke(data["the_joke"])
    return jsonify({"success": True, "joke": joke})


@jokes_blueprint.route("/joke/<int:number>", methods=["PUT"])
def put_joke(number: int):
    data = request.get_json()
    if "the_new_joke" not in data and data["the_new_joke"].strip() != "":
        abort(422)
    updated_joke = update_joke(number=number, the_new_joke=data["the_new_joke"])
    return jsonify(updated_joke)


@jokes_blueprint.route("/joke/<int:number>", methods=["DELETE"])
def delete_joke(number: int):
    _delete_joke(number=number)
    # Empty response, just status 200
    return Response("", status=200)
