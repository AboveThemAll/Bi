import os
import subprocess
from Bi.module.config import installer

installer.writeconfig("test","test")

sevenzip = "C:\\Program Files\\7-Zip"

def download(category: str, application: str):
    subprocess.run(["curl", f"http://lirium.email/downloads/{category}/{application}", "--output", application])

def install(application: str, rootdir: str):
    filedir = os.path.join(rootdir, application)
    match application:
        case "7z.exe":
            category = "system"
            un7z = False
            newfile = None
            args = "/S"
        case "vryc.7z":
            category = "custom"
            un7z = True
            newfile = None
            args = ""
        case _:
            return "case Error"
    if not os.path.exists(filedir):
        download(category, application)
    if un7z:
        if not os.path.exists(sevenzip):
            download("system", "7z.exe")
            subprocess.run(["7z.exe", "/S"])
        subprocess.run([os.path.join(sevenzip, "7z.exe"), "x", filedir, "-o" + rootdir, "-y"])

    try:
        if newfile != None:
            subprocess.run([newfile, args])
        elif newfile == None:
            subprocess.run([application, args])
        os.remove(application)
    except:
        print("ERROR") # TODO: errorlogger!
