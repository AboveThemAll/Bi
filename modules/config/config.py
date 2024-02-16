import configparser
import modules.utils.logger as logger


def writeconfig(section: str, option: str, content: str,file:str):
    config = configparser.ConfigParser()
    config.read(file)
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, option, content)
    with open(file, "w") as config_file:
        config.write(config_file)


def readconfig(section: str, option: str,file:str):
    config = configparser.ConfigParser()
    config.read(file)
    return config.get(section, option, fallback=None)

def replyconfig(file:str):
    config = configparser.ConfigParser()
    config.read(file)
    config_dict = {}
    for section in config.sections():
        config_dict[section] = {}
        for option in config.options(section):
            config_dict[section][option] = config.get(section, option)
    return config_dict


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
