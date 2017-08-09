#coding:utf8

def Info(s):
    if type(s) == str:
        print(s.decode("utf8").encode("gbk"))
    else:
        print(s)

if __name__ == "__main__":
    Info("测试")
