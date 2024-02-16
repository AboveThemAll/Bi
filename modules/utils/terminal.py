import json

from colorama import init

init(autoreset=True)


# Should do the same as os.system("cls") or os.system("clear") just for both windows and linux
def clear_screen():
    print("\033[H\033[J", end="")


def getprograms():
    return #0bock