import os
import module.install.installfiles as installfiles
import module.tweak.tweaker as tweaker
import module.config.installer as installer
import module.config.toggleprograms as toggleprogram

class info:
    mainver = "1"
    hotfixver = "0"
    version = mainver + "." + hotfixver

def main():
    print("SetupTool")
    if os.path.exists("installing.ini"):
        step = installer.readconfig("State", "Step")
        if step == "0":
            while True:
                action = input("What do you want to do?\n[1] Install [2] Tweak [3] Config\n")
                if action == "1":
                    os.system("cls")  # Assuming you're working on a Windows platform
                elif action == "2":
                    os.system("cls")
                elif action == "3":
                    os.system("cls")
                else:
                    os.system("cls")
                    print("Invalid action")
    else:
        installer.writeconfig("State", "Step", "0")

