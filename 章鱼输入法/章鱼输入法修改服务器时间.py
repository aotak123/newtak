# coding=utf-8
import urllib2
import time
####################——————tak制作  vol.611——————####################

# 定义基础url
url = "http://test-zhangyu3.zhihuizhangyu.cn/spring-boot-update-time/timeOper/updateTime?date="

while True:
    type = raw_input("\n 请输入数字：\n 1：查询时间\n 2：恢复时间\n 3：修改时间\n")
    if type == "0":
        continue

    if type == "1":
        urls = "http://test-zhangyu3.zhihuizhangyu.cn/spring-boot-update-time/timeOper/getTime"  # 章鱼输入法获取服务器时间
        request = urllib2.Request(urls)
        response = urllib2.urlopen(request)
        print"当前服务时间："
        print (response.read())
        # break

    if type == "2":
        nowtime = time.strftime('%Y-%m-%d%%20%H:%M:%S')
        fullurl2 = url  + nowtime
        # print fullurl
        request = urllib2.Request(fullurl2)
        response = urllib2.urlopen(request)
        print"已恢复当前服务时间："
        print (response.read())
        # break

    if type == "3":
        while True:  # 无限循环语句
            nowtime = time.strftime('%Y-%m-%d%%20%H:%M:%S')
            print "例如：" + nowtime
            yeartime = raw_input("请输入你想修改的时间：            ！！！请复制例子进行修改时间！！！\n恢复当前时间请输入：0\n")
            #请使用例子中的格式，不得有误
            if yeartime == "0":
                nowtime = time.strftime('%Y-%m-%d%%20%H:%M:%S')
                nowtimeurl = url + nowtime
                # print nowtimeurl
                request = urllib2.Request(nowtimeurl)
                response = urllib2.urlopen(request)
                print (response.read())
                break

            else:
                fullurl3 = url + yeartime
                # print fullurl3
                request = urllib2.Request(fullurl3)
                response = urllib2.urlopen(request)
                print (response.read())

    elif type > "3":
        continue