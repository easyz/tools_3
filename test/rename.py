#coding:gbk

from PIL import Image
import json
import os
import shutil
import time
import math

import re

def RenameRule01(rule):
	return lambda name : rule.replace("*", name)

def RenameRule02(name):
	return "_" + name

def ReDir(dirName, ruleFunc):
    dirName = dirName.decode("utf8").encode("gbk")
    for f in os.listdir(dirName):
        old = os.path.join(dirName, f)
        if os.path.isdir(old):
            new = os.path.join(dirName, ruleFunc(f))
            print(old.replace(dirName, "") + " >>> " + new.replace(dirName, ""))
            os.rename(old, new)

def RefileName(inDirName, outDirName, fileName, ruleFunc = None):
    old = os.path.join(inDirName, fileName)
    new = fileName
    if os.path.isfile(old):
        nameArray = fileName.split(".")
        if not os.path.exists(outDirName):
            os.makedirs(outDirName)
        if ruleFunc:
            new = ruleFunc(nameArray[0]) + "." + nameArray[1]
        newPath = os.path.join(outDirName, new)
        print(old + " >>> " + newPath)
        os.rename(old, newPath)
    return new

def Refiles(dirName, ruleFunc):
    dirName = dirName.decode("utf8").encode("gbk")
    for f in os.listdir(dirName):
    	old = os.path.join(dirName, f)
    	if os.path.isfile(old):
    		nameArray = f.split(".")
    		new = os.path.join(dirName, ruleFunc(nameArray[0])) + "." + nameArray[1]
    		print(old.replace(dirName, "") + " >>> " + new.replace(dirName, ""))
    		os.rename(old, new)

def ReAllfiles(dirName, ruleFunc):
    t = "tmp" + str(int(time.time()))
    alldirs = []
    for root, dirs, files in os.walk(dirName):
        for filePath in files:
            tmpDir = root.replace(dirName, dirName + t)
            newFilePath = RefileName(root, tmpDir, filePath, ruleFunc)
            alldirs.append({
                "tmpDir": tmpDir,
                "root": root,
                "filePath": newFilePath
            })
    for data in alldirs:
        RefileName(data["tmpDir"], data["root"], data["filePath"])
    shutil.rmtree(dirName + t)
    

# ReDir("D:\\develop\\xntg_resource\\切图文件\\翅膀\\", RenameRule01("wing*"))
# ReDir("D:\\develop\\xntg_resource\\切图文件\\角色\\", RenameRule01("body*"))
# ReDir("D:\\develop\\xntg_resource\\切图文件\\武器\\", RenameRule01("weapon*"))
# ReDir("D:\\develop\\xntg_resource\\切图文件\\坐骑\\", RenameRule01("horse*"))

# Refiles("D:\\develop\\xntg\\assets\\dev\\movie\\ring", lambda name : "ring" + name.split("_")[0])
# Refiles("D:\\develop\\xntg\\assets\\dev\\movie\\hitEff", lambda name : "hit" + name.split("_")[0])
# ReAllfiles("E:\\lycq\\resource\\总美术上传文件\\武器\\圣剑", lambda name : str(100000 + (int(name) + 1))[1:])

def ReplaceVName(name):
    matchObj = re.match(r'.*(_v\d+)', name, re.M|re.I)
    if matchObj:
        return name.replace(matchObj.group(1), "")
    else:
        print(name + " not match !!!!!!!!!")
    return name
# ReAllfiles("D:\\develop\\xntg\\client\\project\\resource\\assets\\atlas_ui", ReplaceVName)

# Refiles("D:\\develop\\xntg\\client\\project\\resource\\assets\\atlas_ui\\suit", lambda name : ReplaceVName(name.replace("ui_", "ui_icon_suit_")))
# Refiles("D:\\develop\\xntg\\client\\project\\resource\\assets\\atlas_ui\\image\\icon\\item", lambda name : ReplaceVName(name.replace("ui_", "ui_icon_item_")))
# Refiles("D:\\develop\\xntg\\client\\project\\resource\\assets\\atlas_ui\\image\\skill", lambda name : ReplaceVName(name.replace("ui_", "ui_skill_")))
# Refiles("D:\\develop\\xntg\\client\\project\\resource\\assets\\atlas_ui\\image\\skill\\grey", lambda name : ReplaceVName(name.replace("ui_", "ui_skill_g_")))

def Replace2(name):
    nameid =  int(name)
    nametype = math.floor(nameid / 10000)
    if nametype == 2:
        return str(30000 + nameid % 10000)
    return name

ReAllfiles("G:\\develop\\project\\xntg_resource\\切图文件", Replace2)