# coding:utf8

import urllib
import os

# url = 'https://cdnali.xmxy.jingyuyouxi.net/gameVer/resource/ui/image/skillName/s14_v1.png'
#local = url.split('/')[-1]
# local = "f:\\sdfsdfsdf.png"
# urllib.urlretrieve(url,local,Schedule)

def DownloadFile(url, saveDir):
    fileUrl = url.replace("https://", "").replace("http://", "")
    filePath = "/".join(fileUrl.split("/")[1:])
    fileDir = os.path.join(saveDir, os.path.dirname(filePath))
    filePath = os.path.join(saveDir, filePath)
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)
    def Schedule(a,b,c):
        '''''
        a:已经下载的数据块
        b:数据块的大小
        c:远程文件的大小
        '''
        per = 100.0 * a * b / c
        if per > 100 :
            per = 100
        print url + ('  %.2f%%' % per)
    urllib.urlretrieve(url, filePath, Schedule)

OUT_DIR = "f:\\test_download"
# DownloadFile("https://cdnali.xmxy.jingyuyouxi.net/gameVer/resource/ui/image/skillName/s14_v1.png", "f:\\test_download")
alllines = open("E:\\project\\tools_2\\test\\download_list.log", "r").readlines()
for path in alllines:
    DownloadFile(path.replace("\n", ""), OUT_DIR)