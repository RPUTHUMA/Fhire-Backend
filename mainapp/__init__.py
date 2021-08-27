# -*- coding: utf-8 -*-
"""MLOD backend module"""
from flasgger import Swagger
from flask import Flask, g
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from .config import config
from .views import PingView, UserView
from .utils import create_db_config


# pylint: disable=invalid-name, too-many-format-args
application = Flask(__name__)
CORS(application)
application = create_db_config(application)

db = SQLAlchemy(application)
Migrate(application, db)


def db_session():
    """Method for making session _AppCtxGlobals"""
    g.db_session = db.session()
    g.db = db


# pylint: disable=unused-argument
def simple(env, resp):
    """Method that returns invalid url"""
    resp(b"200 OK", [(b"Content-Type", b"text/plain")])
    return [b"Please re-verify the URL. Check if context path is present"]


application.before_request_funcs = {None: [db_session]}

# this is defining the app with context path
application.wsgi_app = DispatcherMiddleware(
    simple, {config.get("flask", "base_url"): application.wsgi_app}
)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "F-Hire Backend",
        "description": "REST API's for interacting with backend",
        "version": "1.0.0",
    },
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "backend",
            "route": "/docs/backend.json".format(config.get("flask", "base_url")),
        }
    ],
    "static_url_path": "/flasgger_static".format(config.get("flask", "base_url")),
    "swagger_ui": True,
    "specs_route": "/docs".format(config.get("flask", "base_url")),
    "basePath": "/fhire/api",
}

swag = Swagger(application, config=swagger_config, template=swagger_template)


# register apis
application.add_url_rule(
    "/v1/ping",
    view_func=PingView.as_view("Ping"),
    methods=["GET"],
)
application.add_url_rule(
    "/v1/create_user",
    view_func=UserView.as_view("User_rc"),
    methods=["POST"],
)
application.add_url_rule(
    "/v1/validate_user/<string:user_id>",
    view_func=UserView.as_view("User_lc"),
    methods=["GET"],
)
