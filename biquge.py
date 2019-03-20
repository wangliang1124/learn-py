# -*- coding:UTF-8 -*-
import requests
import sys
from bs4 import BeautifulSoup
"""
类说明:下载《笔趣看》网小说《一念永恒》
"""


class downloader(object):
    def __init__(self):
        self.host = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names = []  # 存放章节名
        self.urls = []  # 存放章节链接
        self.nums = 0  # 章节数

    # 获取章节链接
    def get_download_url(self):
        req = requests.get(url=self.target)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[16:])  # 剔除不必要的章节，并统计章节数
        for each in a[16:]:
            self.names.append(each.string)
            self.urls.append(self.host + each.get('href'))

    # 获取章节内容
    def get_contents(self, target):
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', {'class': 'showtxt'})
        texts = texts[0].text.replace('\xa0' * 8, '\n\n')
        return texts

    # 写入文件
    def writer(self, name, path, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


# 主程序启动
if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《一年永恒》开始下载：')
    len = len(dl.names)
    for i in range(len):
        dl.writer(dl.names[i], './download/一念永恒.txt',
                  dl.get_contents(dl.urls[i]))
        sys.stdout.write(" 已下载:%.3f%%" % float(i / len) + '\r')
        # sys.stdout.write(" 已下载:{.3f}% ".format(float(i/len(names)))
        sys.stdout.flush()
    print('《一年永恒》下载完成')
