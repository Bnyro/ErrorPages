import requests
import shutil
import os

targetFolder = "dist/"

def createFile(error):
    fileName = targetFolder + error["value"] + ".html"
    shutil.copy("template.html", fileName)

    filedata = None
    with open(fileName, "r") as f:
        filedata = f.read()

    filedata = filedata.replace("$ErrorCode", error["value"])
    filedata = filedata.replace("$ErrorName", error["description"])

    with open(fileName, "w") as f:
        f.write(filedata)

json = requests.get("https://webconcepts.info/concepts/http-status-code.json").json()

if not os.path.exists(targetFolder):
    os.mkdir(targetFolder)

for error in json["values"]:
    if int(error["value"]) >= 400:
        createFile(error)
