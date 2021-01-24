#!/usr/bin/python
# -*- coding:UTF-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取文件
desktop_path = 'C:\cs\ws\Lottery/'

df = pd.read_table(desktop_path+'hun.txt', header=None, sep=',')
# print df
# print df[1:3]
# print df.loc[0:10,:]
# print df.loc[:,1:6]
tdate = sorted(df.loc[:, 0])
# print tdate
h1 = df.loc[:, 1]
h2 = df.loc[:, 2]
h3 = df.loc[:, 3]
h4 = df.loc[:, 4]
h5 = df.loc[:, 5]
h6 = df.loc[:, 6]

# 将数据合并到一起
all = h1.append(h2).append(h3).append(h4).append(h5).append(h6)
alldata = list(all)
print(len(alldata))

fenzu = pd.value_counts(all, ascending=False)
print(fenzu)

x = list(fenzu.index[:])
y = list(fenzu.values[:])
print(x)
print(y)

# print type(fenzu)
plt.figure(figsize=(10, 6), dpi=70)
plt.legend(loc='best', )

# plt.plot(fenzu,color='red')
plt.bar(str(x), y, alpha=.5, color='r', width=0.8)
plt.title('The red ball number')
plt.xlabel('red number')
plt.ylabel('times')
plt.grid(True)

# 循环，为每个柱形添加文本标注
# 居中对齐
for xx, yy in zip(x,y):
    plt.text(xx, yy+0.5, str(yy), ha='center')


plt.show()