# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import sys, requests

class Download(object):
    def __init__(self):
        self.server         = 'https://www.biqukan.com/'
        self.target         = 'https://www.biqukan.com/1_1094/'
        self.chapter_name   = []
        self.chapter_url    = []
        self.chapter_nums   = 0
        pass
    def get_novel(self):
        req             = requests.get(url = self.target)
        req.encoding    = 'gbk'
        html            = req.text
        bs_html         = BeautifulSoup(html, 'html.parser')
        listmain        = BeautifulSoup(str(bs_html.find_all('div', class_='listmain')[0]), 'html.parser')
        listmain_a      = listmain.find_all('a')

        self.chapter_nums = len(listmain_a[13:-2])
        for each in listmain_a[13:-2]:
            sub_url = str(each.get('href')).lstrip('/')
            self.chapter_name.append(each.string)
            self.chapter_url.append(self.server + sub_url)

    def get_text(self,target):
        req             = requests.get(url = target)
        req.encoding    = 'gbk'
        html            = req.text
        bs_html         = BeautifulSoup(html, 'html.parser')
        text            = bs_html.find_all('div', class_='showtxt')[0].text.replace('\xa0'*8,'\n\n')
        return text

    def write_file(self,path,name,text):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = Download()
    dl.get_novel()
    print('开始下载:')
    for index in range(dl.chapter_nums):
        dl.write_file('一念永恒.txt',dl.chapter_name[index],dl.get_text(dl.chapter_url[index]))
        sys.stdout.write('已下载:%.3f%%' % float(index / dl.chapter_nums) + '\r')
        sys.stdout.flush()
    print('下载结束！')