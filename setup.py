# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="detect-app-backend",
    version="1.0.0",
    description="REST API's for Detect App",
    url="https://github.com/deveshcode/MLDetectionApp",
    author="Devesh Surve",
    author_email="deveshssurve@gmail.com",
    classifiers=["Programming Language :: Python :: 3.6.9"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "celery==4.3.0",
        "flasgger==0.9.3",
        "flask==1.1.1",
        "flask-cors==3.0.8",
        "gunicorn==19.9.0",
        "marshmallow==2.19.5",
        "mysql-connector-python==8.0.17",
        "numpy",
        "pandas",
        "pyjwt==1.7.1",
        "requests-toolbelt==0.9.1",
        "sqlalchemy==1.3.5",
        "socketIO_client==0.7.2",
        "pylint==2.4.4",
        "Cython==0.29.15",
        "vine==1.3.0",
        "Flask-SQLAlchemy==2.4.4",
        "psycopg2-binary",
        "Flask-Migrate==2.5.2"
    ]
)
