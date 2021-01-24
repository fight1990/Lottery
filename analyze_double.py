#!/usr/bin/python
# -*- coding:UTF-8 -*-

#导入需要的包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator
from sklearn import datasets,linear_model
from sklearn.linear_model import LogisticRegression

#读取文件
desktop_path = 'C:\cs\ws\Lottery/'

df = pd.read_table(desktop_path+'hun.txt',header=None,sep=',')

#读取日期
tdate = sorted(df.loc[:,0])

#将以列项为数据，将球号码取出，写入到csv文件中，并取50行数据
# Function to red number to csv file
def RedToCsv(h_num,num,csv_name):
    h_num = df.loc[:,num:num].values
    h_num = h_num[5000::-1]
    #print(len(h_num))
    print(h_num.shape)
    cnt = 0
    #for i in range(len(h_num)):
        #print(h_num[i]) 
        #h_num[i] = str(h_num[i]).replace(" ",'').replace("'",'').replace(')','').replace('[','').replace(']','').replace('"','')
        #print(h_num[i])
        #cnt = cnt + 1
        #print(cnt)
    h_num.reshape(-1,1)
    print(h_num.shape)
    renum2 = pd.DataFrame(h_num)
    renum2.to_csv(csv_name,header=None)
    fp = open(csv_name,'r')
    s = fp.read()
    fp.close()
    a = s.split('\n')
    a.insert(0, 'numid,number')
    s = '\n'.join(a)
    fp = open(desktop_path+csv_name, 'w')
    fp.write(s)
    fp.close()

#调用取号码函数
# create file
RedToCsv('red1',1,'rednum1data.csv')
RedToCsv('red2',2,'rednum2data.csv')
RedToCsv('red3',3,'rednum3data.csv')
RedToCsv('red4',4,'rednum4data.csv')
RedToCsv('red5',5,'rednum5data.csv')
RedToCsv('red6',6,'rednum6data.csv')
RedToCsv('blue1',7,'bluenumdata.csv')


#获取数据，X_parameter为numid数据,Y_parameter为number数据
# Function to get data
def get_data(file_name):
    data = pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    for single_square_feet ,single_price_value in zip(data['numid'],data['number']):
        X_parameter.append([float(single_square_feet)])
        #print(single_price_value)#.replace(" ",'').replace("'",'').replace(')','').replace('[','').replace(']','').replace('"','')
        #print(float(single_price_value.replace("'",'')))
        if(isinstance(single_price_value,str)):
            Y_parameter.append(float(single_price_value.replace("'",'').replace(")",'')))
        else:
            Y_parameter.append(float(single_price_value))
    return X_parameter,Y_parameter


#训练线性模型
# Function for Fitting our data to Linear model
def linear_model_main(X_parameters,Y_parameters,predict_value):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    #regr = LogisticRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions


#获取预测结果函数
def get_predicted_num(inputfile,num):
    X,Y = get_data(inputfile)
    #predictvalue = 51
    predictvalue = 5000
    predictvalue = np.array(predictvalue).reshape(1, -1)
    result = linear_model_main(X,Y,predictvalue)
    #print("num "+ str(num) +" Intercept value " , result['intercept'])
    #print("num "+ str(num) +" coefficient" , result['coefficient'])
    print("num "+ str(num) +" Predicted value: ",result['predicted_value'])


#调用函数分别预测红球、蓝球
get_predicted_num('rednum1data.csv',1)
get_predicted_num('rednum2data.csv',2)
get_predicted_num('rednum3data.csv',3)
get_predicted_num('rednum4data.csv',4)
get_predicted_num('rednum5data.csv',5)
get_predicted_num('rednum6data.csv',6)

get_predicted_num('bluenumdata.csv',1)


# 获取X,Y数据预测结果
# X,Y = get_data('rednum1data.csv')
# predictvalue = 21
# result = linear_model_main(X,Y,predictvalue)
# print "red num 1 Intercept value " , result['intercept']
# print "red num 1 coefficient" , result['coefficient']
# print "red num 1 Predicted value: ",result['predicted_value']


# Function to show the resutls of linear fit model
def show_linear_line(X_parameters,Y_parameters):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    #regr = LogisticRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.figure(figsize=(12,6),dpi=80)
    plt.legend(loc='best')
    plt.scatter(X_parameters,Y_parameters,color='blue')
    plt.plot(X_parameters,regr.predict(X_parameters),color='red',linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()

#显示模型图像，如果需要画图，将“获取X,Y数据预测结果”这块注释去掉，“调用函数分别预测红球、蓝球”这块代码注释下
# show_linear_line(X,Y)