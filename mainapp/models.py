# -*- coding: utf-8 -*-
import sqlalchemy as sa
from flask import g
from .utils import uuid_generator, default_status
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class ModelMixin:
    """Base table for mosaic ai"""

    id = sa.Column(sa.String(100), primary_key=True, default=uuid_generator)

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            if getattr(self, key):
                setattr(self, key, val)


class Users(Base, ModelMixin):
    """ Table for storing user login information"""
    __tablename__ = 'fhire_users'
    id = sa.Column(sa.String(100), primary_key=True, default=uuid_generator)
    first_name = sa.Column(sa.String(100), nullable=False)
    last_name = sa.Column(sa.String(100))
    password = sa.Column(sa.String(200))
    email_id = sa.Column(sa.String(100))
    user_type = sa.Column(sa.String(10))


class JobDescription(Base, ModelMixin):
    """Table for storing job description provided by recruiter"""
    __tablename__ = "fhire_job_description"
    designation = sa.Column(sa.String(200))
    experience = sa.Column(sa.String(100))
    skill = sa.Column(sa.String(500))
    role = sa.Column(sa.Text, default="")
    jd = sa.Column(sa.Text, default="")
    created_by = sa.Column(sa.String(100), default=lambda: g.useremail)
    created_on = sa.Column(sa.DateTime, default=datetime.utcnow)
    last_modified_by = sa.Column(sa.String(100), default=lambda: g.useremail)
    last_modified_on = sa.Column(
        sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    status = sa.Column(sa.String(50), nullable=False, default=default_status())
