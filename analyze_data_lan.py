#!/usr/bin/python
# -*- coding:UTF-8 -*-

# 调用pandas numpy matplotlib包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取newdata.txt文件
desktop_path = 'C:\cs\ws\Lottery/'

df = pd.read_table(desktop_path+"hun.txt",header=None, sep=',')
# print df
# print df[1:3]    #第2到第3行（索引0开始为第一行，1代表第二行，不包含第四行）
# print df.loc[0:10,:]    #第1行到第9行的全部列
# print df.loc[:,[0,7]]  #全部行的第1和第8列
tdate = sorted(df.loc[:, 0])  # 取第一列数据
# print tdate

tdate1 = []  # 将tdate数据读取到列表中
for i in tdate:
    tdate1.append(i)
print(tdate1)

# s = pd.Series(tdate1, index=tdate1)
s = pd.Series(range(1, len(tdate1) + 1), index=tdate1)  # 将日期转换为对应的数值从1开始
# print s

tblue = list(reversed(df.loc[:, 7]))  # 对数据取反
print(tblue)

fenzu = pd.value_counts(tblue, ascending=False)  # 将数据进行分组统计，按照统计数降序排序
print(fenzu)
x = list(fenzu.index[:])  # 获取蓝色号码
y = list(fenzu.values[:])  # 获得蓝色统计数量
print(x)
print(y)

# print type(fenzu)
plt.figure(figsize=(10, 6), dpi=70)  # 配置画图大小、和细度
plt.legend(loc='best')

# plt.plot(fenzu,color='red')    #线图
plt.bar(x, y, alpha=.5, color='b', width=0.8)  # 直方图参数设置
plt.title('The blue ball number')  # 标题
plt.xlabel('blue number')  # x轴内容
plt.ylabel('times')  # y轴内容

plt.show()  # 显示图