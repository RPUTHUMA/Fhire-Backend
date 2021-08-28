# -*- coding: utf-8 -*-
"""
classes and methods for error handling
"""
from flask import Response, g, jsonify
from werkzeug.exceptions import HTTPException

from .exceptions import FhireException
from .log import logger as log


def schema_validation_error(error):
    """
    Handler for marshmallow schema validation errors

    Args:
        error (Exception): exception object

    Returns:
        Response
    """
    try:
        g.db_session.rollback()
    # pylint: disable=broad-except
    except Exception:
        pass
    return jsonify(error.messages), 400


def internal_server_error(error):
    """
    Handler for any internal server error

    Args:
        error (Exception): exception object

    Returns:
        Response
    """
    # retrieve original exception
    original_exception = getattr(error, "original_exception", None)
    if original_exception:
        error = original_exception

    # log exception
    log.exception(error)

    # rollback
    try:
        g.db_session.rollback()
    # pylint: disable=broad-except
    except Exception:
        pass

    # generate response
    if isinstance(error, FhireException):
        return Response(error.message, status=error.code)
    return Response("Something went wrong"), 500
