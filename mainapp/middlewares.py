# -*- coding: utf-8 -*-
"""
classes and methods for middleware
"""
from flask import g, request

from .log import debug, logger as log
from .config import config
from .exceptions import AuthenticationError
from .constants import Headers
from .utils import uuid_generator


@debug
def authentication():
    """ Authentication middleware """
    # skip auth
    if skip_authentication():
        return

    if all(
            [
                Headers.x_auth_email in request.headers
            ]
    ):
        global_vars(
            request.headers[Headers.x_auth_email],
        )
        return
    log.warning("Authentication failure")
    raise AuthenticationError

@debug
def request_middleware():
    """
    request middleware
    :return:
    """
    if Headers.x_request_id in request.headers:
        g.request_id = request.headers[Headers.x_request_id]
    else:
        g.request_id = uuid_generator()


@debug
def global_vars(useremail):
    """
    set global variables
    :param useremail:  useremail
    """
    g.useremail = useremail

@debug
def skip_authentication():
    """skip auth method"""
    skip_auth = config.get("skip-auth", "url").split(",")
    url = request.url
    if [auth_url for auth_url in skip_auth if auth_url in url]:
        return True
