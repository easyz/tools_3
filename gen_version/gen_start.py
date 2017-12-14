#coding:utf8

import gen_version_file as gen
import compress_img as com
import util as util
import gen_version_code as gen_code
import shutil
import os
import json

def Start(outDir, projectDir, version, root):
    print("gen_start!!!")
    # 版本路径

    STEP00 = "编译代码"
    STEP01 = "拷贝资源"
    STEP02 = "打包图集"
    STEP03 = "压缩图片"
    STEP04 = "生成版本MD5文件"
    STEP05 = "合并库文件"
    STEP06 = "生成版本号文件"
    STEP07 = "新版本文件"

    step = [
        STEP00,

        # STEP01,

        # STEP02,

        # STEP03,

        # STEP05,

        # STEP04,
        # STEP06,
        # STEP07,

    ]

    for s in step:
        print(s.decode("utf8").encode("gbk"))

    if raw_input("continue(y/n)") != "y":
        print("interrupt!!!")
        return

    def index(s):
        for v in step:
            if v == s:
                print(s.decode("utf8").encode("gbk"))
                return True
        return False

    if index(STEP00):
        print("===> STEP00")
        util.BuildScript(projectDir, outDir)

    if index(STEP01):
        print("===> STEP01")
        copyPath = [
            "resource\\cfg",
            "resource\\sound",
            "resource\\assets\\game_start",

            "resource\\assets\\image\\img",
            "resource\\assets\\image\\other",
            "resource\\assets\\map",
        ]

        for path in copyPath:
            print("=> copy " + path)
            util.copyFiles(os.path.join(projectDir, path), os.path.join(outDir, path))

    # 2、打包图集
    if index(STEP02):
        print("===> STEP02")
        atlasDir = "resource\\assets\\atlas_ui"
        gen.PackAtals(projectDir, outDir, atlasDir)
        gen.GenAtalsConfig(os.path.join(projectDir, "resource\\default.res.json"), os.path.join(outDir, atlasDir), os.path.join(outDir, "resource"))
        gen.CompressAtals(os.path.join(outDir, atlasDir))

    # 3、压缩资源
    if index(STEP03):
        print("===> STEP03")
        compressPath = [
            "resource\\assets\\atlas_font",
            "resource\\assets\\image\\item_single",
            "resource\\assets\\image\\vipicon",

            "resource\\assets\\movie\\body",
            "resource\\assets\\movie\\mon_show",
            "resource\\assets\\movie\\monster",
            "resource\\assets\\movie\\role_show",
            "resource\\assets\\movie\\skillEff",
            "resource\\assets\\movie\\uiEffe",
            "resource\\assets\\movie\\weapon",
            "resource\\assets\\movie\\wing",
        ]
        for path in compressPath:
            com.Compress(projectDir, path, outDir)

    if index(STEP04):
        print("===> STEP04")
        gen_code.Gen(outDir, version)

    if index(STEP05):
        print("===> STEP05")
        util.MergerLib(outDir)

    if index(STEP06):
        print("===> STEP06")
        gen_code.GenVersionCodeFile(root, version)

    if index(STEP07):
        print("===> STEP07")
        gen_code.UpNewVersionFile(root, version)

    raw_input("\nfinish!!!")