import configparser

config = configparser.ConfigParser()
config.read("installing.ini")

def writeconfig(section: str, option: str, content: str):
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, option, content)
    with open("installing.ini", "w") as config_file:
        config.write(config_file)

def readconfig(section: str, option: str):
    if config.has_section(section) and config.has_option(section, option):
        content = config[section][option]
        return content
    else:
        return None
