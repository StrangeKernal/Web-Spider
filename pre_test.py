# -*- coding:UTF-8 -*-

# request使用测试

import requests

if __name__ == "__main__":
    target = 'https://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url = target)
    req.encoding = 'gbk'
    print(req.text)