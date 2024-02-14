import module.filedownloader as filedownloader
import module.install.installfiles as installfiles
import module.tweak.tweaker as tweaker
import module.config.installer as installer
import os
import json
import platform
#osis = platfrom.platform()
#print(osis) # giebt os aus
class info:
    mainver = "1"
    hotfixver = "0"
    version = mainver + "." + hotfixver
    
def readprograms():
    with open('programs.json',"r") as f:
        content = json.load(f)
    return content

def updateprograms(programs:str):
    with open('programs.json',"r+") as f:
        content = json.load(f)
        match programs:
            case "theia":
                category = "ide"
        state = content[category][programs]
        content[category][programs] = not state
        f.seek(0)
        json.dump(content, f)
        f.truncate()
        return content[category][programs]

def main():
    print("SetupTool")
    if os.path.exists("instaling.ini"):
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
        print("Error")
