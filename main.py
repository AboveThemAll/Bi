import os
import modules.tweak.tweaker as tweaker
import modules.config.config as config
import modules.utils.logger as logger
import modules.utils.terminal as terminal


class info:
    version: str = "1"
    hotfixes: str = "0"
    release = f"{version}.{hotfixes}"


# options in the main menu
# options = {
#    "1": installer.test,
#    "2": tweaker.test,
#    "3": config.test,
#    "4": print("Update CPU/GPU")
# }

def main():
    os.system('Title Brutal Installer')
    if os.path.exists("installing.ini"):
        step = config.readconfig("State", "Step", "installing.ini")
        if step == "0":
            terminal.clear_screen()
            logger.log("RED", "WELCOME TO BRUTAL INSTALLER CLI")
            while True:
                action = input(
                    "What do you want to do?\n[1] Install [2] Tweak [3] Config [4] Update CPU/GPU [q] Quit\n$> ")
                match action:
                    case "1":
                        terminal.clear_screen()
                        logger.log("INFO", "All programs")
                        terminal.getprograms()
                    case "2":
                        terminal.clear_screen()
                        tweaker.test()
                    case "3":
                        terminal.clear_screen()
                        config.test()
                    case "4":
                        terminal.clear_screen()
                        print("update gpu/cpu")  # placeholder
                    case "q":
                        terminal.clear_screen()
                        logger.log("BYE", "See you next time, thank you for using this tool :)")
                        exit()
                # elif action in option does not work
                # if action == 'q':
                #    terminal.clear_screen()
                #    logger.log("BYE", "See you next time, thank you for using this tool :)")
                #    exit()
                # elif action in options:
                #    terminal.clear_screen()
                #    options[action]()
                # else:
                #    terminal.clear_screen()
                #    print("Invalid action")
    else:
        config.writeconfig("State", "Step", "0", "installing.ini")


main()

main.__doc__ = """
Main function for the Brutal Installer CLI.

Prints the setup tool name and checks the current step in the installation process. If the step is 0, it presents a 
menu with different options to perform installation, tweaking, configuration, or updating drivers.

Returns:
    None
"""
