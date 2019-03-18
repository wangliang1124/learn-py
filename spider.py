#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# import cookielib
import urllib3
 
url = "http://www.baidu.com"
http = urllib3.PoolManager()


# response1 = http.request('GET',url)
# print( "第一种方法")
# #获取状态码，200表示成功
# print( response1.status)
# #获取网页内容的长度
# print(response1.data)
 
print( "第二种方法")
#模拟Mozilla浏览器进行爬虫
response2 = http.request('GET',url, headers={'user-agent': 'Mozilla/5.0'})
# #获取状态码，200表示成功
# print( response1.status)
print(response2.headers)
 
# print "第三种方法"
# cookie = cookielib.CookieJar()
# #加入urllib2处理cookie的能力
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# urllib2.install_opener(opener)
# response3 = urllib2.urlopen(url)
# print response3.getcode()
# print len(response3.read())
# print cookie