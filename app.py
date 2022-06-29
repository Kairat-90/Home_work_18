from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.directors import directors_ns
from views.genres import genres_ns

from views.movies import movies_ns


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run(port=8080)
