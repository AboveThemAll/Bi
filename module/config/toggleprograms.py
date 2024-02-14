import json


def toggleprograms(programs:str):
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