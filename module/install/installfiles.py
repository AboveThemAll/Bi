import os

sevenzip = "C:\\Program Files\\7-Zip"

def download(catigory:str,application:str):
    os.system(f"curl http://lirium.email/downloads/{catigory}/{application} --output {application}")

def install(application:str,rootdir:str):
    filedir = f"{rootdir}\\{application}"
    match application:
        case "7z.exe":
            catigory = "system"
            un7z = False
            newfile = None
            args = "/S"
        case "vryc.7z":
            catigory = "custem"
            un7z = True
            newfile = None
            args = ""
        case _:
            return "case Error"
    if not os.path.exists(filedir):
        download(catigory,application)
    if un7z:
        if os.path.exists(sevenzip):
            os.chdir(sevenzip)
            print("test")
            os.system(f"7z.exe x {filedir} -o{rootdir} -y")
            os.chdir(rootdir)
        elif not os.path.exists(sevenzip):
            download("system","7z.exe")
            os.system(f"7z.exe /S")
        else:
            print("un7u Error")
    if args != None:
        if newfile != None:
            os.system(f"{newfile} {args}")
            os.remove(newfile)
            return "Done"
        elif newfile == None:
            os.system(f"{application} {args}")
            os.remove(application)
            return "Done"
        else:
            return "Newfile Error 1"
    elif args == None:
        if newfile != None:
            os.system(f"{newfile}")
            os.remove(newfile)
            return "Done"
        elif newfile == None:
            os.system(f"{application}")
            os.remove(application)
            return "Done"
        else:
            return "Newfile Error 2"
    else:
        return "args Error"