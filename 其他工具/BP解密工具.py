# coding=utf-8

import urllib
import base64
import json

while True:
    #BP解密 （urldecode+base64）
    A = raw_input("请输入加密内容：")
    if type == "":
        continue
    B = urllib.unquote(A)#urldecode解密
    # print(B)
    C = base64.b64decode(B)#base64解密
    print ("\n" + C)

    #json格式化校验
    D = input("\033[1;31m 请复制上面这段返回内容，并黏贴进行格式化校验 \033[0m"+"\n")
    print(json.dumps(D, sort_keys=True, indent=4, ensure_ascii=False))
