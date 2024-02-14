import filedownloader
import installfiles
import tweaker
import configparser
import os
import json

class info:
    mainver = "1"
    hotfixver = "0"
    version = mainver + "." + hotfixver

config = configparser.ConfigParser()
config.read("config.ini")

def writeconfig(section: str, option: str, content: str):
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, option, content)
    with open("config.ini", "w") as config_file:
        config.write(config_file)

def readconfig(section: str, option: str):
    if config.has_section(section) and config.has_option(section, option):
        content = config[section][option]
        return content
    else:
        return None

def readprograms():
    with open('programs.json',"r") as f:
        content = json.load(f)
    return content

def updateprograms(programs:str):
    with open('programs.json',"r+") as f:
        content = json.load(f)
        match programs:
            case "theia":
                category = "ide"
        state = content[category][programs]
        content[category][programs] = not state
        f.seek(0)
        json.dump(content, f)
        f.truncate()
        return content[category][programs]

def main():
    print("SetupTool")
    match readconfig("State","Step"):
        case "0":
            while True:
                match input("What do u wanna do?\n[1]Install [2]Tweak"):
                    case "1" :
                        os.system("clear")
                    case "2":
                        os.system("clear")
                    case _:
                        os.system("clear")
                        print("Invalid action")
