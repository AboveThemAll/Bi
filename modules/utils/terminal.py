import json
import modules.config.toggleprograms as toggleprograms
import modules.utils.terminal as terminal
import modules.utils.logger as logger
from colorama import init, Fore

init(autoreset=True)

#Should do the same as os.system("cls") or os.system("clear") just for both windows and linux
def clear_screen():
    print("\033[H\033[J", end="")


def getprograms():
    while True:
        with open("info.json", "r") as file:
            data = json.load(file)
