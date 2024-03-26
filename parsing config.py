import json
import yaml

class ConfigParser:
    default_json_config_path = "default_config.json"
    default_yaml_config_path = "default_config.yaml"

    @staticmethod
    def parse_json(file_path=None):

        if file_path is None:
            file_path = ConfigParser.default_json_config_path
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("File not found.")
            return None
        except Exception as e:
            print(f"An error occurred while parsing JSON: {e}")
            return None

    @staticmethod
    def parse_yaml(file_path=None):

        if file_path is None:
            file_path = ConfigParser.default_yaml_config_path
        try:
            with open(file_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print("File not found.")
            return None
        except Exception as e:
            print(f"An error occurred while parsing YAML: {e}")
            return None
json_config = ConfigParser.parse_json()
print("Parsed JSON configuration:", json_config)
yaml_config = ConfigParser.parse_yaml()
print("Parsed YAML configuration:", yaml_config)
