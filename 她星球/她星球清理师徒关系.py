# coding=utf-8
import urllib2

####################——————tak制作  vol.611——————####################

# http://10.10.44.27:8020/testcleantools/cleanimei?apptypeid=100012&imei=test20200227   需要vpn
# 106.75.6.212:8020

# while True:
#     a = raw_input("\n 请输入获取的类型：\n 1：测试环境清除\n 2：正式环境清除（无法使用）\n ")
#
#     if a == "1":
#         url = "http://106.75.6.212:8020/testcleantools/cleanimei?apptypeid=100008&imei="
#     if a == "2":
#         # url = "https://invite.crazyccy.com/invite/Iiiii/imei_accid"
#         print ("\033[1;31m 功能暂时无法使用！！！ \033[0m")
#         continue
#     elif a > "2":
#         print("\033[1;31m 输入有误，请重新选择！！！ \033[0m")
#         continue
#     elif a < "1":
#         print("\033[1;31m 输入有误，请重新选择！！！ \033[0m")
#         continue
url = "http://106.75.6.212:8020/testcleantools/cleanimei?apptypeid=100008&imei="
while True:  # 无限循环语句
    imei = raw_input("请输入 \033[1;31m imei\033[0m 或 \033[1;31moaid\033[0m\n返回请输入0\n")
    if imei == "0":
        continue
    if imei == "":
        continue

    if imei == "1":
        imei = "7DD773FA-74C2-455B-A893-C6A3BB8A79D3"
        deviceid = "0019F7F2-A320-44CF-B348-88A5E10E0810"  # "#iphone 7plus

    if imei == "2":
        imei = "863056044142477"  # huawei 8x
        deviceid = "d5412c240eb70ccf"

    if imei == "3":
        imei = "9c6d5e949947422f"  # 黑鲨

    fullurl = url + imei
    # print fullurl
    request = urllib2.Request(fullurl)
    response = urllib2.urlopen(request)
    print (imei + "  " + (response.read()))
