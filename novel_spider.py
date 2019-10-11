# -*- coding:UTF-8 -*-

from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    target = 'https://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    # 此网站采用gbk编码，因此需要对requests.get()获取的对象编码进行调整
    # print(req.text.encode('iso-8859-1').decode('gbk'))    # 临时调整
    req.encoding = 'gbk'                                    # 直接修改
    html = req.text

    bf = BeautifulSoup(html, 'html.parser')

    texts = bf.find_all('div',id='content',class_='showtxt')
    '''
    find_all匹配的返回的结果是一个列表。
    提取匹配结果后，使用text属性，提取文本内容，滤除br标签。
    随后使用replace方法，剔除空格，替换为回车进行分段。 
    在html中是用来表示空格的。replace(‘\xa0’*8,’\n\n’)就是去掉下图的八个空格符号，并用回车代替：
    '''
    texts = texts[0].text.replace('\xa0'*8,'\n\n')          
    __output_File = open('output.txt','w')
    __output_File.write(str(texts))
    __output_File.close()

    