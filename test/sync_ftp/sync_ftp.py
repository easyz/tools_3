# coding:utf8

import os
import re
import time
import datetime
from xfer import *

print("更新远程工程")

curDir = os.path.dirname(__file__)
os.chdir("../../project")
verFile = curDir + "/ver"

def UploadDir(dir):
    if not os.path.exists(dir):
        return False
    xfer = Xfer() 
    xfer.setFtpParams('192.168.28.9', 'client', '123456', "./develop") 
    xfer.upload(dir)   
    return True

def Handle():
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("")
    print("")
    print("###########################################################")
    print("开始检查目录 time：" + nowTime)
    curVersion = 0
    if os.path.exists(verFile):
        fp = open(verFile)
        try:
            curVersion = int(fp.read())
        except Exception as err: 
            pass
        fp.close()

    logFile = curDir + "/tmplog"
    os.system("svn up > " + logFile)

    svnVersion = 0
    if os.path.exists(logFile):
        fp = open(logFile, "r")
        txt = fp.read()
        for s in txt.split("\n"):
            match = re.match(r"At revision (\d+).", s, re.M | re.I)
            if match:
                svnVersion = int(match.group(1))
                break
        print(txt)
        fp.close()
    else:
        print("[ERROR] not log file")

    if svnVersion < 1:
        print("svn 版本 {1}；读取错误".format(svnVersion))
        return

    print("当前记录版本：{0}, svn 版本：{1}".format(curVersion, svnVersion))
    if curVersion == svnVersion:
        return
    print("开始打包工程")
    os.system("egret publish --version temp_upload_folder")


    indexFp = open("./bin-release/web/temp_upload_folder/index.html", "r", encoding='utf-8')
    indexStr = indexFp.readlines()
    indexFp.close()
   
    strList = []
    for line in indexStr:
        if line.find("<!-- 游戏版本 -->") != -1:
            strList.append("<!-- 游戏版本 --> <div style=\"color: #ffffff; position: fixed; top: 0; left: 0; font-size: 40px\">更新时间：" + nowTime + "</div> <!-- 游戏版本 end -->\n")
        else:
            strList.append(line)

    indexStr = "".join(strList)

    indexFp = open("./bin-release/web/temp_upload_folder/index.html", "w", encoding='utf-8')
    indexFp.write(indexStr)
    indexFp.close()

    if UploadDir("./bin-release/web/temp_upload_folder"):
        fp = open(verFile, "w")
        fp.write(str(svnVersion))
        fp.close()
        print("上传成功，版本：" + str(svnVersion))
    else:
        print("上传失败")


if __name__ == "__main__":
    if input("是否自动更新(y/n)") != "y":
        exit()
    while True:
        try:
            Handle()
        except Exception as err: 
            print(err)
        
        time.sleep(5)
    
# UploadDir("./bin-release/web/temp_upload_folder")