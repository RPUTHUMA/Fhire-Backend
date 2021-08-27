import os
import io

from flasgger import swag_from
from flask.views import MethodView
from flask import Flask,Blueprint,request,render_template,jsonify
from datetime import datetime
from flask import Response, g, json, jsonify, request, send_file, send_from_directory

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
        data, errors = schema.load(payload)
        data["type"] = MLType.model
        # save data
        ml_model = models.MLModel(**data)
        g.db_session.add(ml_model)
        g.db_session.commit()
        return "Pong"


    @swag_from("swag/fetch_user.yaml")
    @debug
    def get(self, user_id=None):
        """Get method to get the details of user"""
        return "Pong"
