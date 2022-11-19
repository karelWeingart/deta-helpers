import yaml, os, sys
from os.path import exists


class YamlReader:
    _properties: dict = None
    _DEFAULT_FILE_LOCATION: str = "../app_config.yaml"

    @staticmethod
    def get_configuration() -> dict:

        properties_location = os.path.join(os.path.dirname(__file__), YamlReader._DEFAULT_FILE_LOCATION)

        if YamlReader._properties is None or not exists(properties_location):

            with open(properties_location, "r") as stream:
                try:
                    YamlReader._properties = yaml.safe_load(stream)
                except yaml.YAMLError as e:
                    print(e)

        return YamlReader._properties
