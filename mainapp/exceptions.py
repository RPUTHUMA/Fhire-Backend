# -*- coding: utf-8 -*-
"""
classes and methods for handling exception
"""


class FhireException(Exception):
    """
    FhireException inherited from Exception will be used as base class for all exceptions
    """

    code = 500
    message = "Something went wrong"


class AuthenticationError(FhireException):
    """
    AuthenticationErrorException inherited from FhireException to raise and authentication error
    """

    code = 401
    message = "Please login to continue"


class CreateJobDescriptionException(FhireException):
    """
    class CreateJobDescriptionException(FhireException):
     inherited from FhireException to raise create Job Description exception
    """

    code = 500
    message = "Unable to create Job Description. Please try after some time"


class JobFetchException(FhireException):
    """
    class JobFetchException(FhireException):
     inherited from FhireException to raise Job Fetchexception
    """

    code = 500
    message = "Unable to fetch Job Description. Please try after some time"
