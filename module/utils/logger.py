import os
import sys
from termcolor import colored
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


# Moved outside of the log function
color_map = {
    "SUCCESS": "green",
    "INFO": "white",
    "NOTICE": "grey",
    "DEBUG": "blue",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "magenta",
    "ALERT": "white",
    "BLACK": "black",
    "RED": "red",
    "GREEN": "green",
    "YELLOW": "yellow",
    "BLUE": "blue",
    "MAGENTA": "magenta",
    "CYAN": "cyan",
    "WHITE": "white",
    "GREY": "dark_grey",
    "LIGHTGREY": "light_grey",
    "SIMPLELOGGER": "cyan"
}


def log(level: str, message: str):
    os.system('color')

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    color = color_map.get(level.upper(), "white")  # Default color is white
    print(colored(f"[{timestamp}] [{level.upper()}] {message}", color))
    if level.upper() == "SIMPLELOGGER":
        print(colored("\n    !  Use logger.log the next time for a better visual experience while reading error-logs ^^  !\n", "red"))


def gol(message: str):
    log("SIMPLELOGGER", message)



def test():
    log("DEBUG", "TEST (logger.py)")




log.__doc__ = """
Logs a timestamped message with the specified level and colorizes the output.

Args:
    level (str): The log level of the message.
    message (str): The message to be logged.

Returns:
    None

Examples:
    >>> log("INFO", "This is an information message")
    [2022-01-01 12:00:00] [INFO] This is an information message
"""

gol.__doc__ = """
Logs a timestamped message with a virtual "SIMPLELOGGER" level and colorizes the output in cyan.

Args:
    message (str): The message to be logged.

Returns:
    None
"""
