import os
import module.filedownloader as filedownloader
svenzip = "C:\\Program Files\\7-Zip"

def install(application:str,rootdir:str):
    print(os.getcwd())
    filedir = f"{rootdir}\\{application}"
    if os.path.exists(filedir):
        match application:
            case "7z.exe":
                un7z = False
                newfile = None
                args = "/S"
            case "vmware.7z":
                un7z = True
                newfile = None
                args = "/S"
            case _:
                return "case Error"
        if un7z:
            if os.path.exists(svenzip):
                os.chdir(svenzip)
                os.system(f"7z.exe x {filedir} -o{rootdir} -y")
                os.chdir(rootdir)
            elif os.path.exists(svenzip) != True:
                filedownloader.download("system","7z.exe")
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

    else:
        return "File Error"