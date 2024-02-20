import os
import modules.install.installfiles as installfiles
import modules.tweak.tweaker as tweaker
import modules.config.installer as installer
import modules.utils.logger as logger


class info:
    mainver = "1"
    hotfixver = "0"
    version = f"{mainver}.{hotfixver}"

def config():
    print("Config")

def driver():
    print("update driver")

# options in the main menu
options = {
    "1": installfiles.test,
    "2": tweaker.test,
    "3": config,
    "4": driver
}


def clear_screen():
    print("\033[H\033[J", end="")


def main():
    print("SetupTool")
    if os.path.exists("installing.ini"):
        step = installer.readconfig("State", "Step")
        if step == "0":
            clear_screen()
            logger.log("RED", "WELCOME TO BRUTAL INSTALLER CLI")
            while True:
                action = input(
                    "What do you want to do?\n[1] Install [2] Tweak [3] Config [4] Update CPU/GPU [q] Quit\n")
                if action == 'q':
                    clear_screen()
                    logger.log(
                        "CYAN", "See you next time, thank you for using this tool :)")
                    exit()
                elif action in options:
                    clear_screen()
                    options[action]()
                else:
                    # Sollte das gleiche wie "cls" machen nur hoffentlich auch auf linux etc
                    clear_screen()
                    print("Invalid action")
    else:
        installer.writeconfig("State", "Step", "0")


main()


main.__doc__ = """
Main function for the Brutal Installer CLI.

Prints the setup tool name and checks the current step in the installation process.
If the step is 0, it presents a menu with different options to perform installation, tweaking, configuration, or updating drivers.

Returns:
    None
"""