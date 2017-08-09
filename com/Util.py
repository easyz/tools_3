#coding:utf8

import os

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