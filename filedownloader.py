import os

def download(catigory:str,application:str):
    os.system(f"curl http://lirium.email/downloads/{catigory}/{application} --output {application}")
