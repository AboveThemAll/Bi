import os
import module.install.installfiles as installfiles
import module.tweak.tweaker as tweaker
import module.config.installer as installer
import module.utils.logger as logger


class info:
    mainver = "1"
    hotfixver = "0"
    version = f"{mainver}.{hotfixver}"


# options in the main menu

def menu_install():
    installfiles.test()

def menu_tweak():
    tweaker.test()

def menu_config():
    print("Config")


def menu_updatedrivers():
    print("Update CPU/GPU")


def main():
    print("SetupTool")
    if os.path.exists("installing.ini"):
        step = installer.readconfig("State", "Step")
        if step == "0":

            options = {
                "1": menu_install,
                "2": menu_tweak,
                "3": menu_config,
                "4": menu_updatedrivers
            }
            print("\033[H\033[J", end="")
            logger.log("RED", "WELCOME TO BRUTAL INSTALLER CLI")
            while True:
                action = input(
                    "What do you want to do?\n[1] Install [2] Tweak [3] Config [4] Update CPU/GPU [q] Quit\n")
                if action == 'q':
                    print("\033[H\033[J", end="")
                    logger.log("CYAN","See you next time, thank you for using this tool :)")
                    exit()
                elif action in options:
                    print("\033[H\033[J", end="")
                    options[action]()
                else:
                    # Sollte das gleiche wie "cls" machen nur hoffentlich auch auf linux etc
                    print("\033[H\033[J", end="")
                    print("Invalid action")
    else:
        installer.writeconfig("State", "Step", "0")


main()
