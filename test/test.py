import os
import json
import shutil
import PIL.Image as Image
def GetAllImg(fileDir):
    imgList = []
    for fileDir, sub, fileList in os.walk(fileDir):
        for fileName in fileList:
            if fileName.endswith("png"):
                imgList.append(os.path.join(fileDir, fileName))
    return imgList

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

# TestFunc()


# print "_".join("sdfsdf\\asdfsdfxxx".split("\\")) 

# typeData = {"name": "ui_cm_p_gxhd@112_122_212_36"}
# realFilePath = "D:\\develop\\lyb\\assets\\dev\\atlas_ui\\cm\\ui_cm_p_gxhd@112_122_212_36.png"
# if typeData["name"].find("@") != -1:
#     # print("------------")
#     im = Image.open(realFilePath)
#     im.close()
#     print(im.width)
#     print(im.height)
#     print(im)

if __name__ == "__main__":
    # pass
    allSize = 0
    singleSize = []
    allImageList = GetAllImg("D:\\develop\\lyb\\assets\\dev\\movie\\body")
    # print(allImageList)
    for filePath in allImageList:
        im = Image.open(filePath)
        fileSize = im.width * im.height * 8
        allSize = allSize + fileSize
        singleSize.append({"name": filePath, "size": fileSize})
        im.close()
    print(len(allImageList), str(allSize * 0.001 * 0.001) + " Mb")
    def comp(x, y):
        return y["size"] - x["size"]
    singleSize.sort(comp)
    # print(singleSize)
    json.dump(singleSize, open("e:\\test.txt", "w"))
