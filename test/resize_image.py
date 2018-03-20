import PIL.Image as Image
import os
import math
import json

IMG_PATH = "D:\\develop\\lyb\\assets\\art\\movie\\uiEffe\\eff_ui_ch_46.png"
JSON_PATH = "D:\\develop\\lyb\\assets\\art\\movie\\uiEffe\\eff_ui_ch_46.json"
SCALE = 0.66

def round(v):
    # return math.floor(v)
    return v

def ScaleImg(outPath, path, scale):
    img = Image.open(path)
    w = img.size[0]
    h = img.size[1]
    sWidth = int(math.floor(w * scale))
    sHeight = int(math.floor(h * scale))
    img = img.resize((sWidth, sHeight), Image.ANTIALIAS)  
    img.save(os.path.join(outPath, os.path.basename(path)))
    img.close()
    return [sWidth * 1.0 / w, sHeight * 1.0 / h]

def ScaleConfig(outPath, path, scale):
    jsonObject = json.load(open(path, "r"))
    # print(jsonObject["mc"])
    for k in jsonObject["mc"]:
        frames = jsonObject["mc"][k]["frames"]
        for data in frames:
            data["x"] = round(data["x"] * scale[0])
            data["y"] = round(data["y"] * scale[1])
    for k in jsonObject["res"]:
        data = jsonObject["res"][k]
        data["x"] = round(data["x"] * scale[0])
        data["y"] = round(data["y"] * scale[1])
        data["w"] = round(data["w"] * scale[0])
        data["h"] = round(data["h"] * scale[1])
    json.dump(jsonObject, open(os.path.join(outPath, os.path.basename(path)), "w")) 


array = ScaleImg("f:\\", IMG_PATH, SCALE)
print(array)
ScaleConfig("f:\\", JSON_PATH, array)