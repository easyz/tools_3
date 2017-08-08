import os
import shutil

checkDir = "E:\\lycq\\client\\project\\resource\\assets\\atlas2_ui\\chenghao"

file_prefix = "ui_"

for file in os.listdir(checkDir):
	path = os.path.join(checkDir, file)
	os.rename(os.path.join(checkDir, file), os.path.join(checkDir, file_prefix + file))
	print(file + " => " + (file_prefix + file))

raw_input("finish!!!")