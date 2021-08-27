# -*- coding: utf-8 -*-
"""Schemas for Fhire backend views"""
from marshmallow import ValidationError, fields, schema

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
    first_name = fields.Str(
        required=True, error_messages={"required": "name is required"}
    )
    last_name = fields.Str(
        required=True, error_messages={"required": "name is required"}
    )
    email_id = fields.Str(
        required=True, error_messages={"required": "name is required"}
    )
    password = fields.Str(
        required=True, error_messages={"required": "password is required"}
    )
    user_type = fields.Str()

class JobDescriptionSchema(schema.Schema, SchemaMixin):
    """Schema for Job Description"""
    designation = fields.Str()
    experience = fields.Str()
    skill = fields.Str()
    role = fields.Str()
    jd = fields.Str()
    created_by = fields.Str()
    created_on = fields.DateTime(dump_only=True)
    last_modified_by = fields.Str()
    last_modified_on = fields.DateTime(dump_only=True)
