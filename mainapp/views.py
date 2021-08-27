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
    def post(self, user_id=None):
        """Get method to get the details of user"""
        try:
            password = request.form
            email_id = (g.db_session.query(Users).filter(Users.email_id == payload['email_id'])).first()
        except Exception as ex:
            log.exception(ex)
            return "Validation Failed", 500
