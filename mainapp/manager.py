# -*- coding: utf-8 -*-
"""FHIRE manager module"""

from flask import g

from . import models, schemas
from .utils import response_handler
from .constants import Status


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

def get_job_by_id(job_id=None):
    """
    Method to get job id(s)
    :param job_id: unique identifier of job
    :type job_id: str
    :return: response , status code
    """
    # handle read operation
    if job_id:
        # define schema
        schema = schemas.JobDescriptionSchema(strict=True)
        # query data
        fhire_job = (
            g.db_session.query(models.JobDescription)
            .filter(models.JobDescription.id == job_id)
            .filter(models.JobDescription.status == Status.active)
            .first()
        )
        # serialize data
        data, _ = schema.dump(fhire_job)
    else:
        schema = schemas.JobDescriptionSchema(strict=True)
        # query data
        fhire_job = (
            g.db_session.query(models.JobDescription)
            .filter(models.JobDescription.status == Status.active)
            .all()
        )
        # serialize data
        data, _ = schema.dump(fhire_job, many=True)
    response, status_code = response_handler(
        "Job Descriptions retrieved successfully", "success", 200, data
    )
    # send response
    return response, status_code
