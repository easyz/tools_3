# coding:utf8

from configy import *

import gen_version.gen_start as gen_start
import gen_version.gen_version_code as gen_version_code
import os

input = Log.RawInput("开始！！！(Yes/N)")
if input != "Yes":
    print("exit!!!")
    exit()

curVersion = gen_version_code.GetMaxVersion(outDir)
# if curVersion == CODE_BASE:
#     Log.Info("[ERROR] curVersion == CODE_BASE " + str(CODE_BASE))
#     exit()
Log.Info("当前版本号 => " + str(curVersion))

versionDir = os.path.join(outDir, str(curVersion))
if not os.path.exists(versionDir):
    Log.Info("not version dir!!! " + versionDir)
    exit()

gen_start.Start(versionDir, projectDir, curVersion, outDir)