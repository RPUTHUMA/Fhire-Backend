# -*- coding: utf-8 -*-
"""fhire backend constants module"""


class Headers:
    authorization = "Authorization"
    x_auth_email = "X-Auth-Email"
    x_request_id = "X-Request-Id"
    access_control_allow_origin = "Access-Control-Allow-Origin"
    access_control_allow_methods = "Access-Control-Allow-Methods"
    access_control_allow_headers = "Access-Control-Allow-Headers"

class Status:
    """status constants"""

    active = "active"
    inactive = "inactive"
