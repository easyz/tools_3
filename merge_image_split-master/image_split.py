#coding:UTF-8

import PIL.Image as Image
import json
import os

# outDir = "F:\\Test\\res\\skins\\"
# checkDir = "D:\\SourceTree\\egret_project\\egret_project\\client\\project\\resource\\skins\\"

outDir = "F:\\test\\altas_ui\\"
checkDir = "E:\\lycq\\client\\project\\resource\\image\\"

def VerifyDir(path):
	if not os.path.exists(path):
		os.makedirs(path)

def SplitFrame(frameData, image, dirPath):
	bounds = (frameData["x"], frameData["y"], frameData["x"] + frameData["w"], frameData["y"] + frameData["h"])
	oriImage = Image.new("RGBA",(frameData["sourceW"], frameData["sourceH"]))
	cropImage = image.crop(bounds)

	oriImage.paste(cropImage, (frameData["offX"], frameData["offY"]))
	# VerifyDir(os.path.dirname(dirPath))
	# print(os.path.dirname(dirPath))
	print(dirPath)
	oriImage.save(dirPath)

def SplitImage(imageFilePath, outpathDir):

	VerifyDir(outpathDir)

	dirPath = os.path.dirname(imageFilePath)
	image = Image.open(imageFilePath)
	configFilePath = imageFilePath.split(".")[0] + ".json"

	if not os.path.exists(configFilePath):
		print("not found config file => " + configFilePath)
		return

	jsonObject = None
	with open(configFilePath, "r") as f:
		jsonObject = json.load(f)

	if jsonObject == None:
		print("jsonObject is None => " + configFilePath)
		return

	frameDatas = jsonObject["frames"]
	for frameName in frameDatas:
		SplitFrame(frameDatas[frameName], image, outpathDir + "/" + frameName + ".png")

allFileNum = 0  

def ParsePath(level, path):  
    global allFileNum  
    ''''' 
    打印一个目录下的所有文件夹和文件 
    '''  
    # 所有文件夹，第一个字段是次目录的级别  
    dirList = []  
    # 所有文件  
    fileList = []  
    # 返回一个列表，其中包含在目录条目的名称(google翻译)  
    files = os.listdir(path)  
    # 先添加目录级别  
    dirList.append(str(level))  
    for f in files:  
        if(os.path.isdir(path + '/' + f)):  
            # 排除隐藏文件夹。因为隐藏文件夹过多  
            if(f[0] == '.'):  
                pass  
            else:  
                # 添加非隐藏文件夹  
                dirList.append(f)  
        if(os.path.isfile(path + '/' + f)):  
            # 添加文件  
            fileList.append(f)  
    # 当一个标志使用，文件夹列表第一个级别不打印  
    i_dl = 0  
    for dl in dirList:  
        if(i_dl == 0):  
            i_dl = i_dl + 1  
        else:  
            # 打印至控制台，不是第一个的目录  
            # print '-' * (int(dirList[0])), dl  
            # 打印目录下的所有文件夹和文件，目录级别+1  
            # printPath((int(dirList[0]) + 1), path + '/' + dl)  
            ParsePath((int(dirList[0]) + 1), path + '/' + dl)  
    for fl in fileList:  
        # 打印文件  
        # print '-' * (int(dirList[0])), fl  
        # 随便计算一下有多少个文件 
		
		if not fl.endswith(".json"):
			continue

		pngFilePath = path + "/" + str.replace(fl, ".json", ".png")

		if not os.path.exists(pngFilePath):
			continue

		# print(path, fl, pngFilePath, str.replace(pngFilePath, checkDir, outDir))
        
		SplitImage(pngFilePath, str.replace(path, checkDir, outDir))
		allFileNum = allFileNum + 1  


ParsePath(1, checkDir)
