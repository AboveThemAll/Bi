import configparser
import module.utils.logger as logger

config = configparser.ConfigParser()
config.read("installing.ini")


def writeconfig(section: str, option: str, content: str):
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, option, content)
    with open("installing.ini", "w") as config_file:
        config.write(config_file)


def readconfig(section: str, option: str):
    return config.get(section, option, fallback=None)


def test():
    logger.log("DEBUG", "TEST (installer.py)")


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