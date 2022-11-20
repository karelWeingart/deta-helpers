"""Load configuration"""
import os
from os.path import exists

import yaml

_DEFAULT_FILE_LOCATION: str = "../app_config.yaml"


def get_configuration() -> dict:
    """returns yaml config dict for the app. If the file app_config.yaml
    is not found. nothing is returned."""
    properties_location = os.path.join(os.path.dirname(__file__),
                                       _DEFAULT_FILE_LOCATION)

    if exists(properties_location):

        with open(properties_location, "r", encoding="utf-8") as stream:
            try:
                _properties = yaml.safe_load(stream)
            except yaml.YAMLError as exception:
                print(exception)

    return _properties
