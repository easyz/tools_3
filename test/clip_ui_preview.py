# coding:utf8

import os
from PIL import Image
# im1 = Image.open("hero1001.png")
# newImg = im1.crop((10, 10, 80, 80))
# newImg.save("sss.png")

curDir = os.path.dirname(__file__)

def Decode(str):
    return str.decode("utf8").encode("gbk")

imgPath = raw_input(Decode("请输入图片路径：\n"))
# print(imgPath)

def HandleDir(path):
    for a, b, c in os.walk(path):
        for fileName in c:
            HandlePath(os.path.join(a, fileName))
    

def HandlePath(path):
    if path.endswith(".png") or path.endswith(".jpg"):
        im1 = Image.open(path)
        newPath = "" 
        if path.startswith(curDir):
            newPath = path.replace(curDir, curDir + "\\__out__\\")
        else:
            newPath = curDir + "\\__out__\\" + path.split(":")[1]
        if not os.path.exists(os.path.dirname(newPath)):
            os.makedirs(os.path.dirname(newPath))
        newImg = im1.crop((10, 10, 80, 80))
        newImg.save(newPath)
        print(("切图 => " + path))
    else:
        print(("not img => " + path))
            


def Handle(imgPath):
    if not os.path.exists(imgPath):
        print(Decode("不存在文件 => " + imgPath))
        return
    if os.path.isdir(imgPath):
        HandleDir(imgPath)
    elif os.path.isfile(imgPath):
        HandlePath(imgPath)
    else:
        print(Decode("不是文件 => " + imgPath))


Handle(imgPath)


raw_input("finish!!!")