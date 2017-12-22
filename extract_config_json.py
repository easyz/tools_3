import os
import sys
import shutil

EXTRACT_RES_PATH_ROOT = "F:\\game\\release"
EXTRACT_VER_PATH_ROOT = "F:\\game\\release"
OUT_RES_PATH_ROOT = "F:\\temp_out"

dirList = []
for path in os.listdir(EXTRACT_RES_PATH_ROOT):
    try:
        id = int(path)
        dirList.append(id)
    except:
        pass
dirList.sort()
for id in dirList:
    path = os.path.join(EXTRACT_RES_PATH_ROOT, str(id), "md5.json")
    outPath = os.path.join(OUT_RES_PATH_ROOT, str(id), "md5.json")
    if os.path.exists(path) and os.path.isfile(path):
        if not os.path.exists(os.path.dirname(outPath)):
            os.makedirs(os.path.dirname(outPath))
        shutil.copy(path, outPath)

verDirList = []
for path in os.listdir(EXTRACT_VER_PATH_ROOT):
    try:
        if path.find("ver") != -1:
            id = int(path.replace("ver", "").replace(".json", ""))
            verDirList.append(id)
    except:
        pass
verDirList.sort()

verFileName = "ver" + str(verDirList[len(verDirList) - 1]) + ".json"
shutil.copy(os.path.join(EXTRACT_VER_PATH_ROOT, verFileName), os.path.join(OUT_RES_PATH_ROOT, verFileName))

