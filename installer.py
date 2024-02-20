import json
import subprocess



def download(category: str, application: str):
    if category == "iso":
        subprocess.run(["curl", f"http://lirium.email/{category}/{application}.iso", "--output", application])
    subprocess.run(["curl", f"http://lirium.email/{category}/{application}.exe", "--output", application])

def main():
    with open("programs.json","r") as f:
        content = json.load(f)
    for category in content:
        for app in content[category]:
            if content[category][app]:
                download(category,app)


main()

download.__doc__ = """
Downloads a file from the specified category and saves it with the given application name.

Args:
    category (str): The category of the file to download.
    application (str): The name of the file to download.

Returns:
    None
"""