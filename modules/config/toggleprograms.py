import json
import modules.utils.logger as logger

def toggleprograms(programs: str):
    with open('info.json', "r+") as f:
        content = json.load(f)
        programcategory = str(content["category"][programs]).strip()
        state = content["programs"][programcategory][programs]
        content["programs"][programcategory][programs] = not state
        f.seek(0)
        json.dump(content, f)
        f.truncate()
    return content["programs"][programcategory][programs]


def test():
    logger.log("DEBUG", "TEST (toggleprograms.py)")



toggleprograms.__doc__ = """
Toggles the state of a program in the configuration.

Args:
    programs (str): The name of the program to toggle.

Returns:
    bool: The new state of the program.

Examples:
    >>> toggleprograms("myprogram")
    True
"""