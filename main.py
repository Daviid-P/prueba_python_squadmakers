from flask import Flask

app = Flask(__name__)

from routes.swagger import swagger_blueprint
from routes.jokes import jokes_blueprint
from routes.maths import maths_blueprint
from errors.http_errors import http_errors_blueprint


def main():
    app.register_blueprint(swagger_blueprint)
    app.register_blueprint(jokes_blueprint)
    app.register_blueprint(maths_blueprint)
    app.register_blueprint(http_errors_blueprint)
    app.run(debug=True)


if __name__ == "__main__":
    main()
