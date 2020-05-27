# coding=utf-8
import urllib2
####################——————tak制作  vol.527——————####################

# 获取验证码
# 定义基础url
# url = "http://u.yiqibuduoduo.com/login/main_login/testtool" #步多多正式获取链接
# url = "http://test-u.yiqibuduoduo.com/login/main_login/testtool"#步多多测试获取链接
# 用户输入的类型+手机号
key = "sLQq2_jaKLknsqAwZ"#后台使用的key

while True:
    type = raw_input("\n 请输入获取的类型：\n 1：测试登录\n 2：测试绑定\n 3：正式登录\n 4：正式绑定\n")

    if type == "1":
        url = "http://test-u.yiqibuduoduo.com/login/main_login/testtool"

    if type == "2":
        url = "http://test-u.yiqibuduoduo.com/login/main_login/testtool"

    if type == "3":
        type = "1"
        url = "http://u.yiqibuduoduo.com/login/main_login/testtool"

    if type == "4":
        type = "2"
        url = "http://u.yiqibuduoduo.com/login/main_login/testtool"

    while True:  # 无限循环语句
        mobile = raw_input("请输入要查询的手机号\返回请输入0\n")
        if mobile == "0":
            break
        fullurl = url + "?key=" + key + "&type=" + type + "&mobile=" + mobile
        # print fullurl
        request = urllib2.Request(fullurl)
        response = urllib2.urlopen(request)
        print "验证码："
        print (response.read())
