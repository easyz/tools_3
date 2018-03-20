#coding:utf8

from PIL import Image
import json
import os

def Crop(im1, savePath, cropSize, center):
    im_crop = im1.crop(cropSize)
    IMG_SIZE = (512, 512)
    offset = ((IMG_SIZE[0] >> 1) + center[0], (IMG_SIZE[1] >> 1) + center[1])
    saveImg = Image.new("RGBA", IMG_SIZE)
    saveImg.paste(im_crop, offset)
    saveImg = saveImg.transpose(Image.FLIP_LEFT_RIGHT)  
    fileDir = os.path.dirname(savePath)
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)
    saveImg.save(savePath)

def LoadConfig(filePath):
    jsonData = json.load(open(filePath, "r"))
    mcData = jsonData["mc"]
    for frameName in mcData:
        frameData = mcData[frameName]
        for data in frameData["frames"]:
            data["crop"] = jsonData["res"][data["res"]]
    return mcData

# Crop("F:\\test_download\\gameVer\\resource\\model\\body\\1001\\d\\ani_v2.png", "f:\\he.png",  [0, 230, 85, 230 + 56], (0, 0))
# Crop(Image.open("F:\\test_download\\gameVer\\resource\\model\\body\\1001\\d\\ani_v2.png"), "f:\\he.png", [0, 230, 85, 230 + 56], (0, 0))
# config = LoadConfig("F:\\test_download\\gameVer\\resource\\model\\body\\1001\\d\\ani_v2.json")
# print(config)

def Handle(dir, root, imgPath, jsonPath, outRoot):
    imgFilePath = os.path.join(root, imgPath)
    jsonPath = os.path.join(root, jsonPath)
    configData = LoadConfig(jsonPath)

    imgDir = os.path.dirname(imgPath)
    imgDir = imgDir.replace("\\d", "\\")
    imgDir = imgDir.replace("\\u", "\\")
    nameIndex = 0

    im1 = Image.open(imgFilePath)
    for frameName in configData:
        frameData = configData[frameName]
        if frameName == "stand":
            nameIndex = 1
        elif frameName == "run":
            nameIndex = 9
        elif frameName == "attack":
            nameIndex = 17
        elif frameName == "hit":
            nameIndex = 33
        elif frameName == "die":
            nameIndex = 34
        for data in frameData["frames"]:
            crop = data["crop"]
            Crop(im1, os.path.join(outRoot, imgDir, str(900000 + dir * 10000 + nameIndex)[1:] + ".png"), [crop["x"], crop["y"], crop["x"] + crop["w"], crop["y"] + crop["h"]], (data["x"], data["y"]))
            nameIndex = nameIndex + 1
    im1.close()
    print(">>>>>>>>>>> " + imgPath)

# Handle(3, "F:\\test_download\\gameVer", "resource\\model\\body\\1001\\d\\ani_v2.png", "resource\\model\\body\\1001\\d\\ani_v2.json", "F:\\tmp_out")

ROOT = "F:\\test_download\\gameVer"
ROOT_BODY = "resource\\model\\horse"

def HandlDir(path, dir, root):
    if not os.path.exists(path):
        return
    pngFile = None
    jsonFile = None
    for f in os.listdir(path):
        if f.endswith(".png"):
            pngFile = f
        elif f.endswith(".json"):
            jsonFile = f
    if pngFile != None and jsonFile != None:
        pngFile = os.path.join(path.replace(root + "\\", ""), pngFile)
        jsonFile = os.path.join(path.replace(root + "\\", ""), jsonFile)
        Handle(dir, root, pngFile, jsonFile, "F:\\tmp_out")


for f in os.listdir(os.path.join(ROOT, ROOT_BODY)):
    dir1 = os.path.join(ROOT, ROOT_BODY, f, "u")
    dir3 = os.path.join(ROOT, ROOT_BODY, f, "d")
    HandlDir(dir1, 1, ROOT)
    HandlDir(dir3, 3, ROOT)