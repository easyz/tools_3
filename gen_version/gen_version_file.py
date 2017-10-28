#coding:utf8

import os
import shutil
import hashlib
import json
import PIL.Image as Image
import util
import compress_img as com

WORK = os.path.dirname(__file__)

def CheckDir(dir):
	if not os.path.exists(dir):
		os.makedirs(dir)
		return
	if not os.path.isdir(dir):
		os.makedirs(dir)

def MoveFile(src, dst):
	dir = os.path.dirname(dst)
	CheckDir(dir)
	shutil.move(src, dst)

# def RemoveDir(dir):
# 	for root, dirs, files in os.walk(dir):
# 		for name in files:
# 			os.remove(os.path.join(root, name))
# 		for name in dirs:
# 			os.rmdir(os.path.join(root, name))



# 解析九宫格数据
def ParserSliceData(keyName, jsonData):
	names = keyName.split("@")
	if len(names) < 2:
		return False
	for name in names:
		array = name.split("_")
		if len(array) > 0:
			# 检查数据的正确性
			for value in array:
				try:
					int(value)
				except:
					array = []
					break
			# 检查结果
			if len(array) > 0:
				left = int(array[0])
				top = len(array) < 2 and left or int(array[1])
				right = len(array) < 3 and left or int(array[2])
				bottom = len(array) < 4 and top or int(array[3])

				x = left
				y = top
				width = jsonData["sourceW"] - right - left
				height = jsonData["sourceH"] - bottom - top

				jsonData["scale9grid"] = "{0},{1},{2},{3}".format(x, y, width, height)
				print("scale9grid => " + keyName)
				return True
	return False

# 解析九宫格json数据
def ParserSliceArea(path):
	jsonData = json.load(file(path))
	imageName = jsonData["meta"]["image"]
	oldFrames = jsonData["frames"]
	newFrames = {}
	for frameData in oldFrames:
		temp = {}
		newFrames[frameData["filename"].split(".")[0]] = temp
		temp["x"] = frameData["frame"]["x"]
		temp["y"] = frameData["frame"]["y"]
		temp["w"] =  frameData["frame"]["w"]
		temp["h"] = frameData["frame"]["h"]
		temp["offX"] = frameData["spriteSourceSize"]["x"]
		temp["offY"] = frameData["spriteSourceSize"]["y"]
		temp["sourceW"] = frameData["sourceSize"]["w"]
		temp["sourceH"] = frameData["sourceSize"]["h"]
	jsonData = {}
	jsonData["file"] = imageName
	jsonData["frames"] = newFrames

	frames = jsonData["frames"]
	hasSlice = 0
	for name in frames:
		if ParserSliceData(name, frames[name]):
			hasSlice = hasSlice + 1
	# if hasSlice > 0:
	# 	json.dump(jsonData, file(path, "w"))
	# 重写配置
	json.dump(jsonData, file(path, "w"))

def PackSingleAtals(root, filedir, outDir):
	CheckDir(outDir)
	dir = os.path.join(root, filedir)
	if not os.path.isdir(dir):
		print(dir + " not dir!!!")
		return
	dirName = dir.split("\\")[-1]
	exePath = os.path.join(WORK, "libs\\texturepack\\bin\\TexturePacker.exe")
	packImgList = []
	fullPackImgList = []
	imgList = []
	for fileName in os.listdir(dir):
		filePath = os.path.join(dir, fileName)
		if fileName.endswith(".jpg"):
			print("copy jpg => " + filePath)
			imgList.append(filePath)
			continue
		if not fileName.endswith(".png"):
			continue
		image = Image.open(filePath)
		# 太大的图片忽略
		if image.width * image.height >= 450 * 200:
			imgList.append(filePath)
			print("ignore image ", filePath, image.size)
			continue
		packImgList.append(fileName)
		fullPackImgList.append(os.path.join(filedir, fileName))
		# packImgList.append(fileName)
	CheckDir(dir.replace(root, outDir))
	if len(fullPackImgList) == 1:
		imgList.append(fullPackImgList[0])
		fullPackImgList = []
	if len(fullPackImgList) > 0:
		# 打包图集
		jsonPath = os.path.join(dir.replace(root, outDir), dirName + ".json")
		pngPath = os.path.join(dir.replace(root, outDir), dirName + ".png")
		argsArray = [
			"--disable-rotation",
			"--size-constraints AnySize",
			"--max-width 2048",
			"--max-height 2048",
			"--format json-array",
		]
		command = exePath + " {0} --data {1} --sheet {2} {3}".format(" ".join(argsArray), jsonPath, pngPath, " ".join(packImgList))
		# print(command)
		curDir = os.getcwd()
		os.chdir(filedir)
		os.system(command)	
		os.chdir(curDir)
		ParserSliceArea(jsonPath)
		# os.chdir(curDir)
	for file in imgList:
		shutil.copy2(file, file.replace(root, outDir))

def CopyImg(root, dir, outDir):
	for parent, dirnames, filenames in os.walk(dir):
		for filename in filenames:
			path = os.path.join(parent, filename)
			newPath = path.replace(root, outDir)
			CheckDir(os.path.dirname(newPath))
			# print(path, newPath)
			shutil.copy2(path, newPath)

def PackAtals(root, dir, outDir):
	# if os.path.exists(outDir):
	# 	shutil.rmtree(outDir)
	CheckDir(outDir)
	dir = os.path.join(root, dir)
	imgList = []
	for child in os.listdir(dir):
		path = os.path.join(dir, child)
		# 忽略的目录
		# if child == "garbage":
		# 	continue
		# 不需要打包的目录
		if child == "image" or child == "garbage":
			CopyImg(root, path, outDir)
		else:
			# pass
			if os.path.isdir(path):
				# print(root, os.path.join(dir, child))
				PackSingleAtals(root, os.path.join(dir, child), outDir)

# 重新设置图集的配置
def ResetAtalsConfig(root, prefixRoot, prefix, outDir):
	print("reset atals config")
	configName = "resource\\default.res.json"
	jsonData = json.load(file(os.path.join(root, configName), "r"))
	resJsonData = jsonData["resources"]
	jsonData["resources"] = []
	newResJsonData = []
	# 移除旧的配置
	for data in resJsonData:
		if not data["url"].startswith(prefix):
			newResJsonData.append(data)
	# 增加新的配置文件
	checkDir = os.path.join(outDir, prefixRoot, prefix.replace("/", "\\"))
	# 读取新生成的文件目录	
	for parent, dirnames, filenames in os.walk(checkDir):
		for filename in filenames:
			# 文件路径
			realFilePath = os.path.join(parent, filename)
			# 配置路径
			filePath = os.path.join(parent, filename).replace(checkDir, prefix).replace("\\", "/")
			fileType = "image"
			if filename.endswith(".json"):
				fileType = "sheet"

			# 如果是sheet的图片，不添加到列表
			if fileType == "image" and realFilePath.endswith(".png") and os.path.exists(realFilePath.replace(".png", ".json")):
				continue
			typeData = {
				"url": filePath,
				"type": fileType,
				"name": util.GetFileName(filePath) + (fileType == "sheet" and "_json" or "")
			}
			# 增加图集元素
			if fileType == "sheet":
				frameJsonData = json.load(file(realFilePath, "r"))
				sheetArray = []
				for sheetKey in frameJsonData["frames"]:
					sheetArray.append(sheetKey)
				typeData["subkeys"] = ",".join(sheetArray)
			newResJsonData.append(typeData)

	jsonData["resources"] = newResJsonData
	json.dump(jsonData, file(os.path.join(outDir, configName), "w"))

def CompressAtals(outCheckDir):
	com.CompressOrigen(outCheckDir)

if __name__ == "__main__":
	# path = "F:\\web\\temp_upload\\1\\release\\1\\resource\\assets\\atlas2_ui\\cm\\cm_2_1.json"
	# jsonObject = json.load(file(path, "r"))
	# frames = jsonObject["frames"]
	# for name in frames:
	# 	if ParserSliceData(name, frames[name]):
	# 		print(name)
	# print(jsonObject)
	pass