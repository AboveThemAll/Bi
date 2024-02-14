import module.install.installfiles as installfiles
import module.tweak.tweaker as tweaker
import module.config.installer as installer
import module.config.toggleprograms as toggleprogram
import os

#import platform
#osis = platfrom.platform()
#print(osis) # gibt os aus

class info:
    mainver = "1"
    hotfixver = "0"
    version = mainver + "." + hotfixver



def main():
    print("SetupTool")
    if os.path.exists("installing.ini"):
        match installer.readconfig("State","Step"):
            case "0":
                while True:
                    match input("What do u wanna do?\n[1]Install [2]Tweak [3]Config"):
                        case "1" :
                            os.system("cls")                            
                        case "2":
                            os.system("cls")
                        case "3":
                            os.system("cls") 
                        case _ :
                            os.system("cls")
                            print("Invalid action")
    elif not os.path.exists("installing.ini"):
        installer.writeconfig("State","Step","0")
    else:
        print("Error in main.py(ca Zeile 38)")
