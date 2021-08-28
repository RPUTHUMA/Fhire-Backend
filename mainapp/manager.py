# -*- coding: utf-8 -*-
"""FHIRE manager module"""

from flask import g

from . import models, schemas
from .utils import response_handler
from .constants import Status
from .log import debug, logger as log


@debug
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

@debug
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

@debug
def update_jd(payload, job_id):
    """
    Method to update a given jd
    :param payload: payload provided by user with values to change
    :type : dict
    :param job_id: id of job
    :type job_id: str
    :return: response object
    """
    # define schema
    schema = schemas.JobDescriptionSchema(strict=True)
    # validate data
    data, _ = schema.load(payload, partial=True)
    # query data
    fhire_jd = (
        g.db_session.query(models.JobDescription)
        .filter(models.JobDescription.id == job_id)
        .filter(models.JobDescription.status == Status.active)
        .first()
    )
    # update data
    for key, val in data.items():
        setattr(fhire_jd, key, val)
    # save data
    g.db_session.add(fhire_jd)
    response, status_code = response_handler(
        "Job Description updated successfully", "success", 200
    )
    return response, status_code

@debug
def delete_jd(job_id):
    """
    Method to delete a jd
    :param job_id: id of jd
    :type: str
    :return: response object
    """
    # update data to make soft delete by setting jd status as inactive
    g.db_session.query(models.JobDescription).filter(models.JobDescription.id == job_id).update(
        {"status": Status.inactive}
    )
    g.db_session.commit()
    response, status_code = response_handler(
        "Job Description deleted successfully", "success", 204
    )
    # send response
    return response, status_code

@debug
def forget_password(payload):
    """
    Method to validate and update new password
    :param payload: Dictionary containing
        user email(Str): email
        password(Str): password
    :type payload: JSON
    :return: response , status code
    """
    schema = schemas.UsersSchema(strict=True)
    # check if email already exists
    email_id = (g.db_session.query(models.Users).filter(models.Users.email_id == payload['email_id'])).all()
    if len(email_id) > 0:
        g.db_session.query(models.Users).filter(models.Users.email_id == payload['email_id']).update({"password": payload['password']})
        g.db_session.commit()
        response, status_code = response_handler(
            "Password updated successfully", "Success", 201
        )
    else:
        response, status_code = response_handler(
            "Email Id does not exist, Please verify", "Failed", 200
        )
    # send response
    return response, status_code
