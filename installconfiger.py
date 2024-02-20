import json
import clear

cli = True

class info:
    name = "BrutalInstaller"
    version = "0.0.2alpha"

def getstate(app: str, category: str):
    with open('programs.json', "r+") as f:
        content = json.load(f)
        
        if category.lower() in content and app.lower() in content[category.lower()]:
            f.close()
            return f"{app}:{content[category.lower()][app.lower()]}"
        else:
            f.close()
            return f"Information for '{app.lower()}' in category '{category.lower()}' not found."


def toggleprograms(program: str, category: str):
    with open('programs.json', "r+") as f:
        content = json.load(f)
        
        if category.lower() in content:
            state = content[category.lower()][program.lower()]
            content[category.lower()][program.lower()] = not state
            f.seek(0)
            json.dump(content, f, indent=2)
            f.truncate()
            f.close()
        else:
            f.close()
            print(f"Category '{category.lower()}' not found in the JSON.")


def getallenebeld():
    with open("programs.json","r") as f:
        content = json.load(f)
    apps = []
    for category in content:
        for app in content[category]:
            if content[category][app]:
                apps.append(f"{app}:{content[category][app]}")
    return apps



def main():
    try:
        print(f"\033]2;{info.name}\007")
        while True:
            clear.clear()
            if cli:
                choice = input(f"Brutal Installer Installconfig:\n1|System   2|Coding\n3|Misc     4|Gaming\n5|List\n            q|Quit\n$>")
                match choice:
                    case "1":  # System
                        while True:
                            clear.clear()
                            choice = input("Brutal Installer System:\n1|Driver    2|Runtimes\n3|System    4|Remote            q|back\n$>")
                            match choice:
                                case "1":  # Driver
                                    while True:
                                        clear.clear()
                                        category = "driver"
                                        app = input(f"Brutal Installer Driver:\n1| {getstate('1660ti', category)}            q|back\n$>")
                                        match app:
                                            case "q":
                                                break
                                            case "1":
                                                toggleprograms("1660ti", category)
                                case "2":  # Runtimes
                                    while True:
                                        clear.clear()
                                        category = "runtimes"
                                        app = input(f"Brutal Installer Runtimes:\n1| {getstate('Dotnet4', category)}  2| {getstate('Dotnet6', category)}\n3| {getstate('Dotnet7', category)}  4| {getstate('Dotnet8', category)}\n5| {getstate('VSAio', category)}            q|back\n$>")
                                        match app:
                                            case "q":
                                                break
                                            case "1":
                                                toggleprograms("Dotnet4", category)
                                            case "2":
                                                toggleprograms("Dotnet6", category)
                                            case "3":
                                                toggleprograms("Dotnet7", category)
                                            case "4":
                                                toggleprograms("Dotnet8", category)
                                            case "5":
                                                toggleprograms("VSAio", category)
                                case "3":  # System
                                    while True:
                                        clear.clear()
                                        category = "system"
                                        choice = input(f"Brutal Installer System:\n1| {getstate('7zip', category)}  2| {getstate('Winrar', category)}\n3| {getstate('Git', category)}   4| {getstate('Github', category)}            q|back\n$>")
                                        match choice:
                                            case "q":
                                                break
                                            case "1":
                                                toggleprograms("7zip", category)
                                            case "2":
                                                toggleprograms("Winrar", category)
                                            case "3":
                                                toggleprograms("Git", category)
                                            case "4":
                                                toggleprograms("Github", category)
                                case "4":  # Remote
                                    while True:
                                        clear.clear()
                                        category = "remote"
                                        choice = input(f"Brutal Installer Remote:\n1| {getstate('Filezilla', category)}  2| {getstate('Thorium', category)}            q|back\n$>")
                                        match choice:
                                            case "q":
                                                break
                                            case "1":
                                                toggleprograms("Filezilla", category)
                                            case "2":
                                                toggleprograms("Thorium", category)
                                case "q":
                                    break
                    case "2":  # Coding
                        while True:
                            clear.clear()
                            choice = input("Brutal Installer Coding:\n1|IDE               2|Lang\n3|Software-tools    4|VM            q|back\n$>")
                            match choice:
                                case "1":  # IDE
                                    while True:
                                        clear.clear()
                                        category = "ide"
                                        choice = input(f"Brutal Installer IDE:\n1| {getstate('VisualStudio', category)}  2| {getstate('VSCode', category)}\n3| {getstate('Theia', category)}         4| {getstate('PyCharm', category)}\n5| {getstate('IntelliJ', category)}      6| {getstate('Eclipse', category)}\n7| {getstate('Ardunino', category)}            q|back\n$>")
                                        match choice:
                                            case "q":
                                                break
                                            case "1":
                                                toggleprograms("VisualStudio", category)
                                            case "2":
                                                toggleprograms("VSCode", category)
                                            case "3":
                                                toggleprograms("Theia", category)
                                            case "4":
                                                toggleprograms("PyCharm", category)
                                            case "5":
                                                toggleprograms("IntelliJ", category)
                                            case "6":
                                                toggleprograms("Eclipse", category)
                                            case "7":
                                                toggleprograms("Ardunino", category)
                                case "2":  # Lang
                                    while True:
                                        clear.clear()
                                        category = "lang"
                                        choice = input(f"Brutal Installer Lang:\n1| {getstate('Ahk', category)}    2| {getstate('Golang', category)}\n3| {getstate('Java8', category)}  4| {getstate('Java17', category)}\n5| {getstate('Lua', category)}    6| {getstate('Python3-12', category)}\n7| {getstate('Nodejs', category)}            q|back\n$>")
                                        match choice:
                                            case "q":
                                                break
                                            case "1":
                                                toggleprograms("Ahk", category)
                                            case "2":
                                                toggleprograms("Golang", category)
                                            case "3":
                                                toggleprograms("Java8", category)
                                            case "4":
                                                toggleprograms("Java17", category)
                                            case "5":
                                                toggleprograms("Lua", category)
                                            case "6":
                                                toggleprograms("Python3-12", category)
                                            case "7":
                                                toggleprograms("Nodejs", category)
                                case "3":  # Software-tools
                                    while True:
                                        clear.clear()
                                        category = "softwaretools"
                                        choice = input(f"Brutal Installer Software-tools :\n1| {getstate('DetectitEasy', category)}  2| {getstate('IDA', category)}\n3| {getstate('Silverbullet', category)}            q|back\n$>")
                                        match choice:
                                            case "q":
                                                break
                                            case "1":
                                                toggleprograms("DetectitEasy", category)
                                            case "2":
                                                toggleprograms("IDA", category)
                                            case "3":
                                                toggleprograms("Silverbullet", category)
                                case "4":  # VM
                                    while True:
                                        clear.clear()
                                        category = "vm"
                                        choice = input(
                                            f"VM:\n1| {getstate('Vmware17', category)}  2| {getstate('VmBox', category)}            q|back\n$>")
                                        match choice:
                                            case "q":
                                                break
                                            case "1":
                                                toggleprograms("Vmware17", category)
                                            case "2":
                                                toggleprograms("VmBox", category)
                                case "q":
                                    break
                    case "3":  # Misc
                        while True:
                            clear.clear()
                            choice = input("Brutal Installer Misc:\n1|Modding   2|Soicel\n3|Iso       4|Custom            q|back\n$>")
                            match choice:
                                case "1":  # Modding
                                    while True:
                                        clear.clear()
                                        category = "modding"
                                        choice = input(f"Brutal Installer Modding:\n1| {getstate('CheatEngine', category)}            q|back\n$>")
                                        match choice:
                                            case "q":
                                                break
                                            case "1":
                                                toggleprograms("CheatEngine", category)
                                case "2":  # Soicel
                                    while True:
                                        clear.clear()
                                        category = "soicel"
                                        choice = input(f"Brutal Installer Soicel:\n1| {getstate('Discord', category)}            q|back\n$>")
                                        match choice:
                                            case "q":
                                                break
                                            case "1":
                                                toggleprograms("Discord", category)
                                case "3":  # Iso
                                    while True:
                                        clear.clear()
                                        category = "iso"
                                        choice = input(f"Brutal Installer Iso:\n1| {getstate('Debian12', category)}  2| {getstate('Kubuntu', category)}\n3| {getstate('Parrot', category)}    4| {getstate('Rocky', category)}\n5| {getstate('Windows11', category)}  6| {getstate('windows8.1', category)}            q|back\n$>")
                                        match choice:
                                            case "q":
                                                break
                                            case "1":
                                                toggleprograms("Debian12", category)
                                            case "2":
                                                toggleprograms("Kubuntu", category)
                                            case "3":
                                                toggleprograms("Parrot", category)
                                            case "4":
                                                toggleprograms("Rocky", category)
                                            case "5":
                                                toggleprograms("Windows11", category)
                                            case "6":
                                                toggleprograms("windows8.1", category)
                                case "4":  # Custom
                                    while True:
                                        clear.clear()
                                        category = "custom"
                                        choice = input(f"Brutal Installer Custom:\n1| {getstate('GoXlr', category)}  2| {getstate('Vencord', category)}\n3| {getstate('VRY', category)}            q|back\n$>")
                                        match choice:
                                            case "q":
                                                break
                                            case "1":
                                                toggleprograms("GoXlr", category)
                                            case "2":
                                                toggleprograms("Vencord", category)
                                            case "3":
                                                toggleprograms("VRY", category)
                                case "q":
                                    break
                    case "4":  # Gaming
                        while True:
                            clear.clear()
                            choice = input("Brutal Installer Gaming:\n1|Launcher  2|Coming soon ...            q|back\n$>")
                            match choice:
                                case "1":  # Launcher
                                    while True:
                                        clear.clear()
                                        category = "Launcher"
                                        choice = input(f"Brutal Installer Launcher:\n1| {getstate('EpicGames', category)}  2| {getstate('Steam', category)}            q|back\n$>")
                                        match choice:
                                            case "q":
                                                break
                                            case "1":
                                                toggleprograms("EpicGames", category)
                                            case "2":
                                                toggleprograms("Steam", category)
                                case "2":  # Coming soon
                                    print("Brutal Installer Coming Soon....:\nComing soon... ")
                                case "q":
                                    break
                    case "5":
                        while True:
                            clear.clear()
                            apps = getallenebeld()
                            print("Brutal Installer Applist:")
                            for app in apps:
                                print(f"    {app}")
                            if input("\n            q|back\n$>") =="q":
                                break
                    case "q":
                        clear.clear()
                        exit()
            elif not cli:
                break
    except Exception as e:
        clear.clear()
        print(e)


if __name__ == "__main__":
    main()

main.__doc__ = """
Main function for the Brutal Installer CLI.

Prints the setup tool name and checks the current step in the installation process. If the step is 0, it presents a 
menu with different options to perform installation, tweaking, configuration, or updating drivers.

Returns:
    None
"""
