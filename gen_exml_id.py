#coding:utf8

import os
import shutil
import re
import sys

# print(sys.argv)

if len(sys.argv) < 2:
	raw_input("not exml file, exit!!!")
	exit()

filePath = ""
condition = ""

isPublic = False
filePath = sys.argv[1]

if len(sys.argv) == 3:
	condition = sys.argv[2]
	if condition[0] != "-":
		print("arg error => " + condition)
		exit()
	isPublic = condition.find('p') != -1

# print("isPublic => " + str(isPublic))
# print(filePath)
# exit()

if not os.path.exists(filePath):
	raw_input("not found file => " + filePath)
	exit()

try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 

patternEui = re.compile("\{http://ns\.egret\.com/eui\}(\w+)")
patternNs1 = re.compile("\{\*}(\w+)")
# match = patternNs1.match("{*}Button")

def GetType(value):
	match = patternEui.match(value)
	if match:
		return "eui." + match.groups()[0]
	match = patternNs1.match(value)
	if match:
		return match.groups()[0]
	print("not match => " + value)
	return None


# filePath = "E:\\lycq\\client\\project\\resource\\skins\\guildWars\\redbag\\RedBagWinSkin.exml"

# if not os.path.exists(filePath):
# 	raw_input("not found file => " + filePath)
# 	exit()

tab = " "*4

print ""
print tab + "/"*100
print(tab + "// " + os.path.basename(filePath))
print tab +  "/"*100

try: 
	# ET.register_namespace("e", "http://ns.egret.com/eui")
	tree = ET.parse(filePath)     #打开xml文档 
	root = tree.getroot()         #获得root节点  
except Exception, e: 
	print "Error:cannot parse file:country.xml."
	sys.exit(1) 

idContent = []

fieldPrefix = isPublic and "public" or "protected"

def AddId(node):
	attrib = node.attrib
	if attrib.has_key("id"):
		nodeId = attrib["id"] 
		nodeType = GetType(node.tag)
		if nodeType:
			field = tab +"%s %s: %s" % (fieldPrefix, nodeId, nodeType)
			# print("find node => " + field)
			idContent.append(field)

def FindIds(node):
	childrend = node.getchildren()
	if len(childrend) != 0:
		for child in childrend:
			FindIds(child)
	AddId(node)
	
for child in root: 
	FindIds(child)

print("\n".join(idContent))

# SetClipboard("\n".join(idContent))

print tab + "/"*100
print ""
raw_input("finish!!!")