# -*- coding: utf-8 -*-
from uuid import uuid4
from .config import config
from .log import debug, logger as log

def uuid_generator():
    """Method to generate uuid"""
    _uuid = uuid4()
    return str(_uuid)

@debug
def create_db_config(application):
    """creates database configuration"""
    application.config["SQLALCHEMY_DATABASE_URI"] = config.get("database", "url")
    application.config["SQLALCHEMY_ECHO"] = False
    if config.getboolean("testing", "testing"):
        application.config["SQLALCHEMY_POOL_SIZE"] = None
    else:
        application.config["SQLALCHEMY_POOL_SIZE"] = config.getint(
            "database", "pool_size"
        )
    if config.getboolean("testing", "testing"):
        application.config["SQLALCHEMY_POOL_TIMEOUT"] = None
    else:
        application.config["SQLALCHEMY_POOL_TIMEOUT"] = config.getint(
            "database", "pool_timeout"
        )
    application.config["SQLALCHEMY_POOL_RECYCLE"] = config.getint(
        "database", "pool_recycle"
    )
    application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    return application

@debug
def response_handler(message, status, status_code, data=None):
    """ response handler function to generate json response"""
    response = {"message": message, "status": status}
    if data is not None:
        response["data"] = data
    if status == "success":
        return response, status_code
    return response, status_code

@debug
def default_status():
    """ Default status on creation: active"""
    return "active"
