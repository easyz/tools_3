import os
import json
import shutil

# def GetAllImg(fileDir, prefix):
#     imgList = []
#     for fileDir, sub, fileList in os.walk(fileDir):
#         for fileName in fileList:
#             if fileName.endswith("png"):
#                 imgList.append(os.path.join(prefix, fileName))
#     return imgList

# allFile = GetAllImg("E:\\lycq\\client\\project\\resource\\assets\\movie\\body", "resource/assets/movie/body/")
# fd = file("E:/test.txt", "w")
# fd.write(str(allFile))
# fd.close()
# print(allFile)

def Copy(filePath, prefix):
    if not os.path.exists(filePath):
        print("[ERR] -------------------------------------" + filePath)
        return
    # shutil.copyfile(filePath, "f:/test/" + prefix)
    fDir = "f:/test/" + prefix
    if not os.path.exists(fDir):
        os.makedirs(fDir)
    print(filePath)
    shutil.copy2(filePath, fDir)

def CopyFile(prefix, jsonObj):
    for k in jsonObj:
        value = jsonObj[k]
        fName = prefix + k
        if type(value) == int:
            # print(fName, value)
            fPath = "F:/game/release/" + str(value) + "/" + fName
            # print(fPath)
            Copy(fPath, prefix)
            # return
        else:
            CopyFile(fName + "/", value)

# jsonObj = json.load(file("F:\\game\\release\\ver285.json"))
# CopyFile("", jsonObj)
# print(jsonObj)



def TestFunc():
    path = "F:\\web\\temp_upload\\1\\release\\1\\resource\\default_2_1.res.json"
    jsonObject = json.load(file(path, "r"))
    resources = jsonObject["resources"]
    newFrame = {}
    for data in resources:
        if data["type"] == "sheet":
            print(data["url"])
            data["subkeys"] = ",".join(data["subkeys"])
            # newsubkeys = []
            # subkeys = data["subkeys"].split(",")
            # for keyName in subkeys:
            #     newsubkeys.append(keyName.split(".")[0])
            # data["subkeys"] = newsubkeys
    json.dump(jsonObject, file(path, "w"))
    print(path)
    # for root, dirs, files, in os.walk("F:\\web\\temp_upload\\1\\release\\1\\resource\\assets\\atlas2_ui"):
    #     for fileName in files:
    #         if fileName.endswith(".json"):
    #             path = os.path.join(root, fileName)
    #             jsonObject = json.load(file(path, "r"))
    #             frames = jsonObject["frames"]
    #             newFrame = {}
    #             for name in frames:
    #                 newFrame[name.split(".")[0]] = frames[name]
    #             jsonObject["frames"] = newFrame
    #             json.dump(jsonObject, file(path, "w"))
    #             print(path)

TestFunc()