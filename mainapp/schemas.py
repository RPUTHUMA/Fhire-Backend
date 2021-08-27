# -*- coding: utf-8 -*-
"""Schemas for Fhire backend views"""
from marshmallow import ValidationError, fields, schema
from mosaic_utils.ai.encoding_utils import base64_decode, fix_padding


class BytesField(fields.Field):
    """Bytes Field class"""

    def _validate(self, value):
        """Validates input"""
        # pylint: disable=unidiomatic-typecheck
        if type(value) is not bytes:
            raise ValidationError("Invalid input type.")

        if value is None or value == b"":
            raise ValidationError("Invalid value")


# pylint: disable=too-few-public-methods
class SchemaMixin:
    """Schema mixin class"""
    id = fields.Str()


class UsersSchema(schema.Schema, SchemaMixin):
    """Schema for User Login information"""
    name = fields.Str(
        required=True, error_messages={"required": "name is required"}
    )
    password = fields.Str(
        required=True, error_messages={"required": "password is required"}
    )
    type = fields.Str()
