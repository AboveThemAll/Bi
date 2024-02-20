import os
import subprocess
import modules.utils.logger as logger
import modules.config.installer as installer


installer.writeconfig("test", "test", "test")

sevenzip = "C:\\Program Files\\7-Zip"


def download(category: str, application: str):
    subprocess.run(
        ["curl", f"http://lirium.email/downloads/{category}/{application}", "--output", application])


def install(application: str, rootdir: str):
    filedir = os.path.join(rootdir, application)
    match application:
        case "7z.exe":
            category = "system"
            un7z = False
            executable = None
            args = "/S"
        case "vryc.7z":
            category = "custom"
            un7z = True
            executable = None
            args = ""
        case _:
            return "case Error"
    if not os.path.exists(filedir):
        download(category, application)
    if un7z:
        if not os.path.exists(sevenzip):
            download("system", "7z.exe")
            subprocess.run(["7z.exe", "/S"])
        subprocess.run(
            [
                os.path.join(sevenzip, "7z.exe"),
                "x",
                filedir,
                f"-o{rootdir}",
                "-y",
            ]
        )
    try:
        if executable != None:
            subprocess.run([executable, args])
        else:
            subprocess.run([application, args])
        os.remove(application)
    except Exception:
        link = "https://github.com/AboveThemAll/Bi/issues"
        logger.log(
            "ERROR", "There was an error in \"installfiles\.py\(Line\: 53\)\".\nReport this error to the developers on github, please!\n" + link)


def test():
    logger.log("DEBUG", "TEST (installfiles.py)")


download.__doc__ = """
Downloads a file from the specified category and saves it with the given application name.

Args:
    category (str): The category of the file to download.
    application (str): The name of the file to download.

Returns:
    None
"""


install.__doc__ = """
Installs an application in the specified root directory.

Args:
    application (str): The name of the application to install.
    rootdir (str): The root directory where the application will be installed.

Returns:
    None

Raises:
    Exception: If there is an error during the installation process.
"""