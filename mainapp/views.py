# -*- coding: utf-8 -*-
from flasgger import swag_from
from flask.views import MethodView
from flask import Flask, Blueprint, request, render_template, jsonify, g
from datetime import datetime
from flask import Response, g, json, jsonify, request, send_file, send_from_directory
from . import models, schemas
from .schemas import UsersSchema
from .models import Users
from .log import debug, logger as log
from .exceptions import CreateJobDescriptionException
from .manager import create_jd


# pylint: disable=no-self-use, unused-variable
class PingView(MethodView):
    """Class for ping"""

    @swag_from("swag/ping.yaml")
    def get(self):
        """get method to check health of service"""
        return "Pong"


class UserView(MethodView):
    """Class for User"""

    @swag_from("swag/create_user.yaml")
    def post(self):
        """Post method to create a user"""
        try:
            payload = request.json
            schema = schemas.UsersSchema(strict=True)
            # check if email already exists
            email_id = (g.db_session.query(Users).filter(Users.email_id == payload['email_id'])).all()
            if len(email_id) > 0:
                return "Email Id already exists", 500
            data, errors = schema.load(payload)
            user_data = models.Users(**data)
            g.db_session.add(user_data)
            g.db_session.commit()
            return jsonify(data), 201
        except Exception as ex:
            log.exception(ex)
            return "Unable to create user", 500

class ValidateView(MethodView):
    """Class for User"""

    @swag_from("swag/validate_user.yaml")
    def get(self, user_id=None):
        """Get method to get the details of user"""
        try:
            password = request.args.get("password")
            schema = schemas.UsersSchema(strict=True)
            user_detail = (g.db_session.query(Users).filter(Users.email_id == user_id)).first()
            # serialize data
            data, errors = schema.dump(user_detail)
            if data["password"] == password:
                return "User validated successfully", 200
            else:
                return "User validation failed", 500
        except Exception as ex:
            log.exception(ex)
            return "Validation Failed", 500

class JobDescription(MethodView):
    """Class for maintaining Job Description"""

    @swag_from("swag/create_jd.yaml")
    @debug
    def post(self):
        """Post method to create a job description"""
        try:
            payload = request.json
            # calling register recipe
            response, status_code = create_jd(payload)
            # send response
            return jsonify(response), status_code
        except Exception as ex:
            log.exception(ex)
            raise CreateJobDescriptionException
