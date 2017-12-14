# coding:utf8

import os
import sys

sys.path.append(os.path.dirname(__file__) + "/../")

from com.AtlasUtil import *
import com.Log

RES_JSON_PATH = "D:\\develop\\lyb\\client\\project\\resource\\default.res.json"
DEV_FOLDER_PATH = 'D:\\develop\\lyb\\assets\\dev'
COMP_DEV_FOLDER_PATH = 'D:\\develop\\lyb\\assets\\cdev'

def PackAtlasFolder(folderPath, outFolderPath):
    for parent,dirnames,filenames in os.walk(folderPath):
        for dirName in dirnames:
            dirPath = os.path.join(parent, dirName).replace(folderPath, "")[1:]
            PackSingleAtals(folderPath, dirPath, outFolderPath)
    Log.Info("打包完成！！！")

def GenAtalsConfig(resjsonPath, checkDir, outputPath):
    ResetAtalsConfig(resjsonPath, "assets/atlas_ui", checkDir, "assets/atlas_ui", outputPath)

# def CreateFolderLink(folderPath, outFolderPath):
#     for dirName in os.listdir(folderPath):
#         if dirName.find("atlas_ui") != -1:
#             continue
#         os.system("mklink /J " + os.path.join(outFolderPath, dirName) + " " + os.path.join(folderPath, dirName))


# PackAtlasFolder(os.path.join(DEV_FOLDER_PATH, "atlas_ui"), os.path.join(COMP_DEV_FOLDER_PATH, "atlas_ui"))
# CreateFolderLink(DEV_FOLDER_PATH, COMP_DEV_FOLDER_PATH)
GenAtalsConfig(RES_JSON_PATH, os.path.join(COMP_DEV_FOLDER_PATH, "atlas_ui"), COMP_DEV_FOLDER_PATH)