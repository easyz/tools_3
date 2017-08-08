#coding:utf8

import os
import shutil
try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 

rootdir = "E:\\lycq\\client\\project\\resource"

allExmlFiles = []

def FindAll(array, node, name):
	children = node.getchildren()  
	for child in children:
		if child.tag == name:
			array.append(child)
		else:
			FindAll(array, child, name)

def ParserExml(path):
	# print(path)
	tree = ET.parse(path)     #打开xml文档 
	root = tree.getroot()         #获得root节点  

	allSource = []
	array = []
	FindAll(array, root, "{http://ns.egret.com/eui}Image")
	for data in array:
		data = data.attrib
		for key in data:
			# print(key)
			if key.startswith("source"):
				allSource.append(data[key])
	return allSource
				# print(data[key])
		# print(data.attrib)
		# print(data.attrib["source"])
	# print(array)

	# for image in root.findall("Image"):
	# 	print(image)
	# for child in root:
		# print(child)
		# print(child.getchildren())
		# print (child.tag == "{http://ns.egret.com/eui}Image")
		# print child.tag, "---", child.attrib 

for parent,dirnames,filenames in os.walk(rootdir):
	# for dirname in  dirnames:
	# 	print "parent is:" + parent
	# 	print  "dirname is" + dirname

	for filename in filenames:
		if filename.endswith(".exml"):
			allExmlFiles.append(os.path.join(parent,filename))
			# print "parent is :" + parent
			# print "filename is:" + filename
			# print "the full name of the file is:" + os.path.join(parent,filename)


allRes = {}

for filePath in allExmlFiles:
	keys = ParserExml(filePath)
	for key in keys:
		if not allRes.has_key(key):
			allRes[key] = True
	# break


allResArray = []
for key in allRes:
	allResArray.append(key)

# print(allResArray)


def GetAllImage(path):
	dictData = {}
	for parent,dirnames,filenames in os.walk(path):
		for filename in filenames:
			if filename.endswith(".png") or filename.endswith(".jpg"):
				dictData[filename.split(".")[0]] = os.path.join(parent,filename)
	return dictData

allExistImageArray = GetAllImage("E:\\lycq\\resource\\assets\\atlas2_ui")


allImageArray = GetAllImage("F:\\test")
allImage2Array = GetAllImage("E:\\dukto\\h4-docs\\h4-docs\\wudao_meishushuchu")

garbagePath = "E:\\lycq\\resource\\assets\\atlas2_ui\\garbage"
for res in allResArray:
	array = res.split(".")
	res = array[-1]
	if not allExistImageArray.has_key(res):
		if allImageArray.has_key(res):
			shutil.copy(allImageArray[res], garbagePath + "\\")
		elif allImage2Array.has_key(res):
			shutil.copy(allImage2Array[res], garbagePath + "\\")
		else:
			print ("not found " + res)


raw_input("finish!!")