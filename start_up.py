# coding:utf8

# outDir = "F:\\game\\game2\\release"

import gen_version.gen_start as gen_start
import gen_version.gen_version_code as gen_version_code
import com.Log as Log
import os

from configy import *

input = Log.RawInput("提升版本号！！！(Yes/N)")
newVersion = input == "Yes"

# print("工程路径 => " + projectDir)
# print("输出文件路径 => " + outDir)

curVersion = gen_version_code.GetMaxVersion(outDir)
Log.Info("当前版本号 => " + str(curVersion))
if newVersion:
    curVersion = curVersion + 1

    Log.Info("新建版本号 => " + str(curVersion))
    path = os.path.join(outDir, str(curVersion))
    Log.Info("out dir => " + path)
    os.makedirs(path)
else:
    pass
