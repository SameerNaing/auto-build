from datetime import datetime
import yaml


def utf_8_to_string(utf_8_text: str) -> str:
    """Function to convert UTF-8 text to python string

    Args:
        utf_8_text (str): UTF-8 text

    Returns:
        str: Python string
    """
    result = [char for char in utf_8_text if char != "'" and char != "\n"]
    return "".join(result)


def parse_yaml_string(string: str) -> dict:
    """Function to parse yaml data to python dict

    Args:
        string (str): yaml string data

    Returns:
        dict: parsed yaml data in python dict format
    """
    data = yaml.safe_load(string)
    return {
        "build_android": data["build"]["android"]["generate"],
        "android_version_code": data["build"]["android"]["versionCode"],
        "android_version_number": data["build"]["android"]["versionNumber"],
        "build_ios": data["build"]["ios"]["generate"],
        "ios_version_number": data["build"]["ios"]["versionNumber"],
        "ios_build_number": data["build"]["ios"]["buildNumber"]
    }


def format_message_date(date: datetime) -> str:
    return date.strftime("%d %b, %Y %I:%M %p")
