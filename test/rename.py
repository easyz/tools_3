#coding:gbk

from PIL import Image
import json
import os
import shutil
import time

def RenameRule01(rule):
	return lambda name : rule.replace("*", name)

def ReDir(dirName, ruleFunc):
    dirName = dirName.decode("utf8").encode("gbk")
    for f in os.listdir(dirName):
        old = os.path.join(dirName, f)
        if os.path.isdir(old):
            new = os.path.join(dirName, ruleFunc(f))
            print(old.replace(dirName, "") + " >>> " + new.replace(dirName, ""))
            os.rename(old, new)

def RefileName(inDirName, outDirName, fileName, ruleFunc):
    old = os.path.join(inDirName, fileName)
    if os.path.isfile(old):
        nameArray = fileName.split(".")
        if not os.path.exists(outDirName):
            os.makedirs(outDirName)
        new = os.path.join(outDirName, ruleFunc(nameArray[0])) + "." + nameArray[1]
        print(old + " >>> " + new)
        os.rename(old, new)

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
            # alldirs[tmpDir] = root
            alldirs.append({
                "tmpDir": tmpDir,
                "root": root,
                "filePath": filePath
            })
            RefileName(root, tmpDir, filePath, ruleFunc)
    for data in alldirs:
        RefileName(data["tmpDir"], data["root"], data["filePath"], ruleFunc)
    shutil.rmtree(dirName + t)
    

# ReDir("D:\\develop\\xntg_resource\\��ͼ�ļ�\\���\\", RenameRule01("wing*"))
# ReDir("D:\\develop\\xntg_resource\\��ͼ�ļ�\\��ɫ\\", RenameRule01("body*"))
# ReDir("D:\\develop\\xntg_resource\\��ͼ�ļ�\\����\\", RenameRule01("weapon*"))
# ReDir("D:\\develop\\xntg_resource\\��ͼ�ļ�\\����\\", RenameRule01("horse*"))

# Refiles("D:\\develop\\xntg\\assets\\dev\\movie\\ring", lambda name : "ring" + name.split("_")[0])
# Refiles("D:\\develop\\xntg\\assets\\dev\\movie\\hitEff", lambda name : "hit" + name.split("_")[0])
ReAllfiles("E:\\lycq\\resource\\�������ϴ��ļ�\\����\\ʥ��", lambda name : str(100000 + (int(name) + 1))[1:])