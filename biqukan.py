# -*- coding:UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import requests
import collections
import re
import os
import time
import sys
import types
"""
类说明:下载《笔趣看》网小说: url: https://www.biqukan.com/
Parameters:
	target - 《笔趣看》网指定的小说目录地址(string)
    keyword: 小说名称
"""


class Download(object):
    def __init__(self):
        # self.__target_url = target
        self.__head = {
            'User-Agent':
            'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19',
        }

    def get_target_url(self, keyword):
        search_url = 'https://www.biqukan.com/s.php'
        query = {'ie': 'gbk', 's': 2758772450457967865, 'q': keyword}
        res = requests.get(search_url, params=query)
        bs = BeautifulSoup(res.text, 'html5lib')
        booknames = bs.find_all(class_='bookname')
        print('\n')
        print('与“{}”相关的小说'.format(keyword))
        print('索引\t小说名\t\t链接')
        urls = []
        for index, item in enumerate(booknames[:10]):
            if item.a != None:
                download_url = "https://www.biqukan.com" + item.a.get('href')
                bookname = item.string
                print(
                    str(index) + '\t', bookname + '\t\t', download_url + '\t')
                urls.append(download_url)
        if len(urls) > 1:
            index = int(input('请输入索引号：'))
            while index < 0 or index >= len(urls):
                index = int(input('索引号超出范围，请再次输入：'))
            else: return urls[index]
        else:
            return urls.pop()

    """
	函数说明:获取下载链接
	Parameters:
		无
	Returns:
		novel_name + '.txt' - 保存的小说名(string)
		numbers - 章节数(int)
		download_dict - 保存章节名称和下载链接的字典(dict)
	Modify:
		2017-05-06
	"""

    def get_download_url(self, target_url=''):
        charter = re.compile(u'[第弟](.+)章', re.IGNORECASE)
        target_req = request.Request(url=target_url, headers=self.__head)
        target_response = request.urlopen(target_req)
        target_html = target_response.read().decode('gbk', 'ignore')
        listmain_soup = BeautifulSoup(target_html, 'html5lib')
        chapters = listmain_soup.find_all('div', class_='listmain')
        download_soup = BeautifulSoup(str(chapters), 'lxml')
        # print(download_soup.dl.dt, str(download_soup.dl.dt).split("》"))
        novel_name = str(download_soup.dl.dt).split("》")[0][5:]
        flag_name = "《" + novel_name + "》" + "正文卷"
        numbers = (len(download_soup.dl.contents) - 1) / 2 - 8
        download_dict = collections.OrderedDict()
        begin_flag = False
        numbers = 1
        for child in download_soup.dl.children:
            if child != '\n':
                if child.string == u"%s" % flag_name:
                    begin_flag = True
                if begin_flag == True and child.a != None:
                    download_url = "https://www.biqukan.com" + child.a.get(
                        'href')
                    download_name = child.string
                    names = str(download_name).split('章')
                    name = charter.findall(names[0] + '章')
                    if name:
                        download_dict['第' + str(numbers) + '章 ' +
                                      names.pop()] = download_url
                        numbers += 1
        return novel_name + '.txt', numbers, download_dict

    """
	函数说明:爬取文章内容
	Parameters:
		url - 下载连接(string)
	Returns:
		soup_text - 章节内容(string)
	"""

    def get_contents(self, url):
        download_req = request.Request(url=url, headers=self.__head)
        download_response = request.urlopen(download_req)
        download_html = download_response.read().decode('gbk', 'ignore')
        soup_texts = BeautifulSoup(download_html, 'html5lib')
        texts = soup_texts.find_all(id='content', class_='showtxt')
        soup_text = BeautifulSoup(str(texts), 'html5lib').div.text.replace(
            '\xa0', '')
        return soup_text

    """
	函数说明:将爬取的文章内容写入文件
	Parameters:
		name - 章节名称(string)
		path - 当前路径下,小说保存名称(string)
		text - 章节内容(string)
	Returns:
		无
	Modify:
		2017-05-06
	"""

    def Writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write('##\t'+name + '\n\n')
            for each in text:
                if each == 'h':
                    write_flag = False
                if write_flag == True and each != ' ':
                    f.writelines(each)
                if write_flag == True and each == '\r':
                    f.write('\n')
            f.write('\n\n')


if __name__ == "__main__":
    print("\n\t\t欢迎使用《笔趣看》小说下载小工具\n\n\t\t作者:Leon\t时间:2019-03-24\n")
    print(
        "*************************************************************************"
    )

    #实例化下载类
    dl = Download()

    #小说地址
    target_input = str(input("请输入小说目录下载地址或者小说名字:  "))
    target_url = ''

    if target_input.startswith('http:') or target_input.startswith('https:'):
        target_url = target_input
    else:
        target_url = dl.get_target_url(target_input)

    name, numbers, url_dict = dl.get_download_url(target_url)

    if name in os.listdir('./download/'):
        os.remove('./download/' + name)
    index = 1

    #下载中
    print("《%s》下载中:" % name[:-4])
    for key, value in url_dict.items():
        dl.Writer(key, './download/' + name, dl.get_contents(value))
        sys.stdout.write("已下载:%.3f%%" % float(index / numbers) + '\r')
        sys.stdout.flush()
        index += 1

    print("《%s》下载完成！" % name[:-4])
