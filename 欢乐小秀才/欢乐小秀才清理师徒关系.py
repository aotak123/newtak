# coding=utf-8
import urllib2

####################——————tak制作  vol.527——————####################

while True:
    imei = raw_input("请输入 \033[1;31m imei\033[0m 或 \033[1;31moaid\033[0m\n")
    if imei == "0":
        continue
    if imei == "":
        continue
    if imei == "1":
        imei = "359596060310566"  # 三星
        deviceid = "f8a37fcb1c827dce"

    if imei == "2":
        imei = "7DD773FA-74C2-455B-A893-C6A3BB8A79D3"
        deviceid = "0019F7F2-A320-44CF-B348-88A5E10E0810"  # "#iphone 7plus

    if imei == "3":
        # imei = "863056044142477"#huawei 8x
        imei = "7ff3e7df-b96e-e8e1-baf1-f6dcf75f2be3"
        deviceid = "94764aa49bb442e5"
        aaid = "5a2eca205675ce4903d7f8d3881e5a6f"
        oaid = "7ff3e7df-b96e-e8e1-baf1-f6dcf75f2be3"

    if imei == "4":
        # imei = "865973042769010"#黑鲨
        imei = "43e219e4af34ad4e"  # 黑鲨
        deviceid = "43e219e4af34ad4e"

    url = "http://106.75.6.212:8020/testcleantools/cleanimei?apptypeid=100022&imei="
    fullurl = url + imei

    # print fullurl

    request = urllib2.Request(fullurl)
    response = urllib2.urlopen(request)
    print imei + "  " + (response.read())
