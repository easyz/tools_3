# coding:utf8

import com.Log as Log

PLA = "neigou"

if PLA == "fj3":
    outDir = "F:\\game\\game2\\release"
    projectDir = "D:\\develop\\lycq_ad\\client\\project"

    # 游戏id
    GAME_ID = "2"
    # 游戏目录版本号
    CODE_DIR_VERSION = "1"
    # 基础版本号
    CODE_BASE = 1
elif PLA == "neigou":
    outDir = "F:\\game\\game3\\release"
    projectDir = "D:\\develop\\tlzs\\client\\project"

    # 游戏id
    GAME_ID = "3"
    # 游戏目录版本号
    CODE_DIR_VERSION = "1"
    # 基础版本号
    CODE_BASE = 1
else:
    print("------------ no")

Log.Info("输出目录 => " + outDir)
Log.Info("工程目录 => " + projectDir)
Log.Info("游戏id => " + (GAME_ID))
Log.Info("游戏目录版本号 => " + (CODE_DIR_VERSION))
Log.Info("基础版本号 => " + str(CODE_BASE))