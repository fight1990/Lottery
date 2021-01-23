#!/usr/bin/python
# -*- coding:UTF-8 -*-
# coding:utf-8
# author:levycui
# date:20160513
# Description:双色球信息收集

import urllib.request
import urllib.error
from bs4 import BeautifulSoup  # 采用BeautifulSoup
import os
import re


# 伪装成浏览器登陆,获取网页源代码
def getPage(href):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib.request.Request(
        url=href,
        headers=headers
    )
    try:
        post = urllib.request.urlopen(req)
    except Exception:
        print('Error')
        # print(e.code)
        # print(e.reason)

    return post.read()


# 初始化url 双色球首页
url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'


# ===============================================================================
# 获取url总页数
def getPageNum(url):
    num = 0
    page = getPage(url)
    soup = BeautifulSoup(page)
    strong = soup.find('td', colspan='7')
    # print strong
    if strong:
        result = strong.get_text().split(' ')
        # print result
        list_num = re.findall("[0-9]{1}", result[1])
        # print list_num
        for i in range(len(list_num)):
            num = num * 10 + int(list_num[i])
        return num
    else:
        return 0

        # ===============================================================================


file_path = 'C:\cs\ws\Lottery\{}'

# 获取每页双色球的信息
def getText(url):
    for list_num in range(1, getPageNum(url)):  # 从第一页到第getPageNum(url)页
        print(list_num)  # 打印下页码
        href = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' + str(list_num) + '.html'  # 调用新url链接
        # for listnum in len(list_num):
        page = BeautifulSoup(getPage(href))
        em_list = page.find_all('em')  # 匹配em内容
        div_list = page.find_all('td', {'align': 'center'})  # 匹配 <td align=center>这样的内容

        # 初始化n
        n = 0
        # 将双色球数字信息写入num.txt文件
        fp = open(file_path.format("num.txt"), "w")
        for div in em_list:
            emnum1 = div.get_text()
            # print emnum1
            text = div.get_text()
            # text = text.encode('utf-8')

            # print title
            n = n + 1
            if n == 7:
                text = text + '\n'
                n = 0
            else:
                text = text + ','
            fp.write(str(text))
        fp.close()

        # 将日期信息写入date.txt文件
        fp = open(file_path.format("date.txt"), "w")
        for div in div_list:
            text = div.get_text().strip('')
            # print text
            list_num = re.findall('\d{4}-\d{2}-\d{2}', text)
            list_num = str(list_num[::1])
            list_num = list_num[2:12]
            if len(list_num) == 0:
                continue
            elif len(list_num) > 1:
                fp.write(str(list_num) + '\n')
        fp.close()

        # 将num.txt和date.txt文件进行整合写入hun.txt文件中
        # 格式如下：
        # ('2016-05-03', '09,12,24,28,29,30,02')
        # ('2016-05-01', '06,08,13,14,22,27,10')
        # ('2016-04-28', '03,08,13,14,15,30,04')
        #
        fp01 = open(file_path.format("date.txt"), "r")
        a = []
        for line01 in fp01:
            a.append(line01.strip('\n'))
            # print a
        fp01.close()

        fp02 = open(file_path.format("num.txt"), "r")
        b = []
        for line02 in fp02:
            b.append(line02.strip('\n'))
            # print b

        fp02.close()

        # 注意事项：数据替换 去除‘ and " 符号
        fp = open(file_path.format("hun.txt"), "a")
        for cc in zip(a, b):  # 使用zip方法合并
            print(cc)
            fp.write(str(cc) + '\n')
        fp.close()


        # ===============================================================================


if __name__ == "__main__":
    pageNum = getPageNum(url)
    print(pageNum)
    getpagetext = getText(url)
    print(getpagetext)