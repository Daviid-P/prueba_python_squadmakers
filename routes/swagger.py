from flask import Blueprint, redirect, render_template, url_for

swagger_blueprint = Blueprint("swagger_blueprint", __name__)


@swagger_blueprint.route("/")
def root():
    return redirect(url_for(".get_docs"))


@swagger_blueprint.route("/docs")
def get_docs():
    return render_template("swaggerui.html")
