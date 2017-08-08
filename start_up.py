# coding:utf8

outDir = "F:\\game\\release"

import gen_version.gen_start as gen_start
import gen_version.gen_version_code as gen_version_code
import os

input = raw_input("提升版本号！！！(Yes/N)")
newVersion = input == "Yes"

# print("工程路径 => " + projectDir)
print("输出文件路径 => " + outDir)

curVersion = gen_version_code.GetMaxVersion(outDir)
print("当前版本号 => " + str(curVersion))
if newVersion:
    curVersion = curVersion + 1

    print("新建版本号 => " + str(curVersion))
    path = os.path.join(outDir, str(curVersion))
    print("out dir => " + path)
    os.makedirs(path)
else:
    pass
