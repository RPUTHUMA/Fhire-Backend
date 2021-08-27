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
    __tablename__ = "users"
    name = sa.Column(sa.String(100))
    sa.Column("name", sa.String(100), nullable=False)
    sa.Column("password", sa.String(100))
    sa.Column("type", sa.String(20))
