import json

def toggleprograms(programs:str):
    with open('programs.json',"r+") as f:
        content = json.load(f)
        with open('category.json') as c:
            category = json.load(c)
        programcategory = str(category[programs]).strip()
        state = content[programcategory][programs]
        content[programcategory][programs] = not state
        f.seek(0)
        json.dump(content, f)
        f.truncate()
        return content[programcategory][programs]
