import json


def toggleprograms(programs:str):
    with open('programs.json',"r+") as f:
        content = json.load(f)
        match programs:
            case "theia":
                category = "IDE"
            case "vs":
                category = "IDE"
            case "vscode":
                category = "IDE"
            case "arduino":
                category = "IDE"
            case "eclipse":
                category = "IDE"
            case "intelij":
                category = "IDE"
            case "pycharm":
                category = "IDE"
            case "ida":
                category = "cracking"
            case "silverbullet":
                category = "cracking"
            case "die":
                category = "cracking"
            case "goxlr":
                category = "custem"
            case "vryc":
                category = "custem"
            case "vencord":
                category = "custem"
            case "darcula":
                category = "custem"
            case "plugins":
                category = "custem"
            case "parrot":
                category = "iso"
            case "rocky":
                category = "iso"
            case "debian12":
                category = "iso"
            case "kubuntu":
                category = "iso"
            case "openmidavault":
                category = "iso"
            case "rescatux":
                category = "iso"
            case "win8.1":
                category = "iso"
            case "win11":
                category = "iso"
            case "lua":
                category = "lang"
            case "ahk":
                category = "lang"
            case "go":
                category = "lang"
            case "java8":
                category = "lang"
            case "java17":
                category = "lang"
            case "nodejslts":
                category = "lang"
            case "python3.12":
                category = "lang"
        state = content[category][programs]
        content[category][programs] = not state
        f.seek(0)
        json.dump(content, f)
        f.truncate()
        return content[category][programs]