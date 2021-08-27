# -*- coding: utf-8 -*-
"""mosaic ai logs module"""
import logging
import sys
from logging.handlers import RotatingFileHandler

from flask import g, request

from .config import config


# define log formatter
# pylint: disable=invalid-name
log_format = (
    "%(asctime)s - [%(levelname)s] - %(project_id)s - %(request_id)s - %(message)s"
)
formatter = logging.Formatter(log_format)


# define rotating file handler
file_name = config.get("log", "file_name")
file_size = config.get("log", "file_size")
backup_count = config.get("log", "backup_count")
log_level = config.get("log", "level")
file_handler = RotatingFileHandler(
    file_name, maxBytes=int(file_size), backupCount=int(backup_count)
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


# define stream handler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)


# define logger
logger = logging.getLogger("mosaic-ai-backend")
logger.setLevel(log_level)

# add handlers
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
extra = {"project_id": None, "request_id": None}
logger = logging.LoggerAdapter(logger, extra)


def debug(fn):
    """debug method in logs"""
    def wrapper(*args, **kwargs):
        """wrapper for debug"""
        args_specs = locals()
        project_id = None
        request_id = None
        result = None
        if "fn" in args_specs:
            del args_specs["fn"]
        if request:
            args_specs["url"] = request.url
            if not request.files:
                args_specs["json"] = (
                    request.get_json(force=True, silent=True) or request.data
                )
        try:
            project_id = g.project_id
        # pylint: disable=broad-except
        except Exception as e:
            pass
        try:
            request_id = g.request_id
        # pylint: disable=broad-except
        except Exception as e:
            pass
        # pylint: disable=redefined-outer-name
        extra = {"project_id": project_id, "request_id": request_id}
        logger = logging.getLogger("mosaic-ai-backend")
        logger = logging.LoggerAdapter(logger, extra)
        logger.debug("Entering {0} - parameters {1}".format(fn.__qualname__, args_specs))
        try:
            result = fn(*args, **kwargs)
        except Exception as e:
            logger.exception(
                "Exception in {0} - parameters {1}".format(fn.__qualname__, args_specs)
            )
            raise e
        finally:
            logger.debug(
                "Finished {0} - parameters {1}".format(fn.__qualname__, args_specs)
            )
        return result

    return wrapper
