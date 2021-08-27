# -*- coding: utf-8 -*-
"""FHIRE manager module"""

from flask import g

from . import models, schemas
from .utils import response_handler


def create_jd(payload):
    """
    Method to create a new JD
    :param payload: Dictionary containing
        designation(Str): designation looking for the job
        experience(Str): total number of experience required
        skill(Str): Skillset required for the given job
        role(Str): Roles and responsibilities required for the job
        jd(Str): Job Description
    :type payload: JSON
    :return: response , status code
    """
    schema = schemas.JobDescriptionSchema(strict=True)
    data, errors = schema.load(payload)
    jd_data = models.JobDescription(**data)
    g.db_session.add(jd_data)
    g.db_session.commit()
    response, status_code = response_handler(
        "Job Description created successfully", "success", 201, data
    )
    return response, status_code
