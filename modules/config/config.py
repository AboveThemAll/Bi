import modules.utils.logger as logger
import yaml

def readconfig(filepath):
    with open(filepath, 'r') as file:
        config_data = yaml.safe_load(file)
    return config_data


def writeconfig(content, filepath):
    with open(filepath, 'w') as file:
        yaml.dump(content, file)


def test():
    logger.log("DEBUG", "TEST (config.py)")


writeconfig.__doc___ = """
Writes the specified content to the configuration file.

Args:
    section (str): The section in the configuration file.
    option (str): The option within the section.
    content (str): The content to be written.

Returns:
    None
"""
readconfig.__doc___ = """
Reads the value of the specified option from the configuration file.

Args:
    section (str): The section in the configuration file.
    option (str): The option within the section.

Returns:
    str or None: The value of the option if it exists, or None if the section or option is not found.
"""
