from random import randint
from flask import abort
import requests


def get_chuck_norris_joke() -> str:
    res = requests.get(
        "https://api.chucknorris.io/jokes/random",
        headers={"Accept": "application/json"},
    )
    if res.status_code != 200:
        abort(500)
    res_json = res.json()
    return res_json["value"]


def get_dad_joke() -> str:
    res = requests.get(
        "https://icanhazdadjoke.com/",
        headers={"Accept": "application/json"},
    )
    if res.status_code != 200:
        abort(500)
    res_json = res.json()
    if res_json["status"] != 200:
        abort(500)
    return res_json["joke"]


def create_joke(the_joke: str) -> dict:
    return {
        "number": randint(1000, 9999),
        "value": the_joke,
    }


def update_joke(number: int, the_new_joke: str) -> dict:
    if randint(1, 10) == 1:
        abort(500)
    return {"number": number, "string": the_new_joke}


def delete_joke(joke_id: int) -> None:
    pass
