# coding=utf-8
import urllib2
import re
import time
####################——————tak制作  vol.605——————####################


key = "sLQq2_jaKLknsqAwZ"   #后台使用的key
testmobile = '/Users/aotak/Documents/小秀才测试手机号名单.xlsx'
realmobile = '/Users/aotak/Documents/小秀才正式手机号名单.xlsx'


while True:
    type = raw_input("\033[30m \n 请输入验证码类型：\n 1：测试登录\n 2：测试绑定\n 3：正式登录\n 4：正式绑定 \033[0m\n")

    if type == "1":
        url = "http://test-u-hxxc.tt.cn/login/main_login/testtool"
    if type == "2":
        url = "http://test-u-hxxc.tt.cn/login/main_login/testtool"
    if type == "3":
        type = "1"
        url = "https://u.happyxiaoxiucai.com/login/main_login/testtool"
    if type == "4":
        type = "2"
        url = "https://u.happyxiaoxiucai.com/login/main_login/testtool"


    while True:  # 无限循环语句
        mobile = raw_input("\033[30m 请输入要查询的手机号\返回请输入:0 \033[0m \n")
        right = re.match(r"^1[35789]\d{9}$", mobile)
        #手机号都为11位，所以必须限定匹配的数字的位数，通过$来限定以9位数字结尾，又因为手机号都以1开头，所以通过^1限定以1开头，
        #然后手机号第二位貌似只有3,5,6,7,8,这几个数字，所以通过[3,5,7,8,9]来匹配其中的任一数字，后续推出新的号段，需在这里做添加
        #最后｛9｝匹配9个/d。【补】：/d 表示匹配数字

        if mobile == "0":   #返回请输入:0
            break
        # if mobile == "":    #输入空不执行
        #     continue
        if right:
            # print ("检验通过")    #校验手机号打印结果
            fullurl = url + "?key=" + key + "&type=" + type + "&mobile=" + mobile

            print fullurl   #打印请求地址

            request = urllib2.Request(fullurl)   #拼接请求
            response = urllib2.urlopen(request)  #请求链接
            num = response.read()    #读取页面信息
            print ("\033[1;31m 您的验证码： \033[0m" + num)

            if url == "http://test-u-hxxc.tt.cn/login/main_login/testtool":     #测试环境写入手机号纪录
                if num == '查不到！':  #如果接口没有返回没有查到则不记录
                    continue
                else:
                    with open(testmobile,'r+') as file_object:   #打开记录execl文件
                        pi_string = ''
                        for lines in file_object:
                            pi_string += lines.strip()
                        if mobile in pi_string:   #判断手机号是否存在于表内
                            continue   #表内不做写入
                        else:
                            nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')  #获取当前时间
                            file_object.write(mobile + "\t")    #\t = tab  \n = 换行
                            file_object.write(nowtime + "\n")

            if url == "https://u.happyxiaoxiucai.com/login/main_login/testtool":      #正式环境写入手机号纪录
                if num == '查不到！':    #如果接口没有返回没有查到则不记录
                    continue
                else:
                    with open(realmobile,'r+') as file_object: #打开记录execl文件
                        pi_string = ''
                        for lines in file_object:
                            pi_string += lines.strip()
                        if mobile in pi_string:    #判断手机号是否存在于表内
                            continue   #在表内不做写入
                        else:
                            nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')    #获取当前时间
                            file_object.write(mobile + "\t")     # \t = tab  \n = 换行
                            file_object.write(nowtime + "\n")

        else:
            print ("\033[1;31m！！!手机号码错误，请重新输入！！!\033[0m")