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
