# Web-Spider

什么是网络爬虫？

定义：
    网络爬虫（Web Spider）是按规则自动地抓取网站信息的程序或者脚本。

流程：
    1.先由urllib的request打开Url得到网页html文档
    2.浏览器打开网页源代码分析元素节点
    3.通过Beautiful Soup或则正则表达式提取想要的数据
    4.存储数据到本地磁盘或数据库（抓取，分析，存储）

By the way：
    requests库是第三方库，需要我们自己安装。
    requests库的github地址：https://github.com/requests/requests