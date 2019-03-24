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
        # print(html)
        div_bf = BeautifulSoup(html, 'html5lib')
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[16:])  # 剔除不必要的章节，并统计章节数
        for each in a[16:]:
            print(each)
            self.names.append(each.string)
            self.urls.append(self.host + each.get('href'))

    # 获取章节内容
    def get_contents(self, target):
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html, 'html5lib')
        texts = bf.find_all('div', {'class': 'showtxt'})

        if len(texts) > 0 and texts[0].text:
            # texts = texts[0].text.replace('\xa0' * 8, '\n\n')
            texts = texts[0].text
            return texts

    # 写入文件
    def writer(self, name, path, text=''):
        with open(path, 'a', encoding='utf-8') as f:
            if name != None and text != None:
                f.write(name + '\n')
                f.writelines(text)
                f.write('\n\n')


# 主程序启动
if __name__ == "__main__":

    dl = downloader()
    # dl.get_contents('https://www.biqukan.com/1_1094/5514174.html')
    dl.get_download_url()
    print('《一年永恒》开始下载：')
    l = len(dl.names)
    for i in range(l):
        dl.writer(dl.names[i], './download/一念永恒.txt',
                  dl.get_contents(dl.urls[i]))
        dl.writer(dl.names[i], './download/一念永恒目录.txt')
        # sys.stdout.write(" 已下载:%.3f%%" % float(i / l) + '\r')
        sys.stdout.write('已下载:{:.3f}%'.format(float(100 * i / l)) + '\r')
        sys.stdout.flush()
        # print('已下载:{:.3f}'.format(float(i/l)), end= '\r', flush=True)
    print('《一年永恒》下载完成')
