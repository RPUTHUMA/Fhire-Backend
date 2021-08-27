# -*- coding: utf-8 -*-
"""config file for mldetect app"""
import configparser
import os

# pylint: disable=invalid-name
config_file = os.getenv(
    "FHIRE_SETTINGS", "/usr/local/opt/mosaic-ai-backend/configs/local.ini"
)


# define config parser
config = configparser.ConfigParser(allow_no_value=True)
config.read(config_file)
