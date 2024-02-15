import os
import module.install.installfiles as installfiles
import module.tweak.tweaker as tweaker
import module.config.installer as installer

class info:
    mainver = "1"
    hotfixver = "0"
    version = f"{mainver}.{hotfixver}"


def install():
    return

def main():
    print("SetupTool")
    if os.path.exists("installing.ini"):
        step = installer.readconfig("State", "Step")
        if step == "0":
            options = {
                "1": install(),
                "2": print("Tweak"),
                "3": print("Config"),
                "4": print("Update CPU/GPU")
            }
            while True:
                action = input("What do you want to do?\n[1] Install [2] Tweak [3] Config [4] Update CPU/GPU [q] Quit\n")
                if action == 'q':
                    exit()
                elif action in options:
                        options[action]()
                else:
                    print("\033[H\033[J", end="") # Sollte das gleiche wie "cls" machen nur hoffentlich auch auf linux etc
                    print("Invalid action")
    else:
        installer.writeconfig("State", "Step", "0")


main()