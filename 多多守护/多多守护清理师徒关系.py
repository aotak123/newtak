# coding=utf-8
import urllib2

####################——————tak制作  vol.721——————####################
url = "http://106.75.6.212:8020/testcleantools/cleanimei?apptypeid=100031&imei="
while True:  # 无限循环语句
    imei = raw_input("请输入 \033[1;31m imei\033[0m 或 \033[1;31moaid\033[0m\n返回请输入0\n")
    if imei == "0":
        continue
    if imei == "":
        continue
    if imei == "1":
        imei = "359596060310566"  # 三星
        deviceid = "f8a37fcb1c827dce"

    if imei == "2":
        imei = "9CFBCE03-BAE2-42DE-81CF-C537A1AD1D59"
        deviceid = "F95F0A62-8C6E-40B5-ABE2-D855D49742F1"  # "#iphone 7plus

    if imei == "3":
        # imei = "863056044142477"#huawei 8x
        imei = "7ff3e7df-b96e-e8e1-baf1-f6dcf75f2be3"
        deviceid = "94764aa49bb442e5"
        aaid = "461f14fe628616f42a085259e39cc978"
        oaid = "7ff3e7df-b96e-e8e1-baf1-f6dcf75f2be3"

    if imei == "4":
        # imei = "865973042769010"#黑鲨
        imei = "43e219e4af34ad4e"  # 黑鲨
        deviceid = "43e219e4af34ad4e"

    fullurl = url + imei
    # print fullurl
    request = urllib2.Request(fullurl)
    response = urllib2.urlopen(request)
    print (imei + "  " + (response.read()))
