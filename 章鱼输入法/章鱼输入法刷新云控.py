# coding=utf-8
import urllib2
####################——————tak制作  vol.527——————####################

# 定义基础url
url = "https://test-zhangyu3.zhihuizhangyu.cn/zycloudcontrol/cloud.basis?pwd=147147"
request = urllib2.Request(url)
response = urllib2.urlopen(request)
# print (response.read())
print"刷新成功"



