#coding:utf8

import os
import shutil

def GetAllFile(path, includeSuffix):
    if not os.path.exists(path):
        print(" not dir " + path)
        return []
    if includeSuffix == None:
        print("include suffix == null")
        return []
    imgList = []
    for fileName in os.listdir(path):
        filePath = os.path.join(path, fileName)
        for suf in includeSuffix:
            if fileName.endswith(suf):
                imgList.append(filePath)
                continue
    return imgList

def CheckDir(dir):
    if os.path.exists(dir):
        return
    os.makedirs(dir)

def ClearDir(dir):
    if not os.path.exists(dir) or not os.path.isdir(dir):
        return
    for fName in os.listdir(dir):
        fPath = os.path.join(dir, fName)
        if os.path.isdir(fPath):
            shutil.rmtree(fPath)
        else:
            os.remove(fPath)

def ClearAndCheckDir(dir):
    CheckDir(dir)
    ClearDir(dir)