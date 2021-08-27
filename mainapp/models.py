# -*- coding: utf-8 -*-
import sqlalchemy as sa
from .utils import uuid_generator
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ModelMixin:
    """Base table for mosaic ai"""

    id = sa.Column(sa.String(100), primary_key=True, default=uuid_generator)

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            if getattr(self, key):
                setattr(self, key, val)


class Users(Base, ModelMixin):
    __tablename__ = 'Users'
    id = sa.Column(sa.String(100), primary_key=True, default=uuid_generator)
    first_name = sa.Column(sa.String(100), nullable=False)
    last_name = sa.Column(sa.String(100))
    password = sa.Column(sa.String(200))
    email_id = sa.Column(sa.String(100))
    user_type = sa.Column(sa.String(10))
