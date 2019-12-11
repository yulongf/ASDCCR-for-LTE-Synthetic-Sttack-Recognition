#!/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd
import math
import numpy as np

#计算某一列某个范围内的条件熵
def HD0 (da,x,y,z,w): #参数为data，即原始数据集,x为范围选择下限，y为范围选择上限，z为列的特征属性,w为类别标签
    D0 = da[[z, 40]][(da[z] >= x) & (da[z] < y)]  #得到第一列0到0.1之间的数和对应的类别标签列
    F0 = D0[z][(D0[40]==w)] #得到0到0.1之间类别标签为w的数
    total, d, f = len(da), len(D0), len(F0) #total指数据集总条数，d指数据集中0到0.1的条目，f指0到10数据中类别为0的数据条目
    #print total, d, f
    if d-f == 0 or d == 0 or f == 0:
        HD = 0
    else:
        HD = (float(d)/total)*((-float(f)/d)*math.log(float(f)/d,2)-float((d-f)/d)*math.log(float(d-f)/d,2))
    return HD

#计算b类a列的条件熵
def compute (dt,a,b):#第b个类别的第a个特征属性
    tha = 10
    i = 0.0
    D = 0.0
    j = 0
    #print dt[a]
    while (1):
        D = D + HD0(dt, i, i + 10,a,b)
        i = i + 10
        j = j + 1
        if j >= math.ceil(float(dt[a].max())/10):
            break
    return D

#计算类0的条件熵列表，即正常数据
def SeriHD (dta):
    counts = dta[40].value_counts() #原始数据集每个类别的记录
    liCon = [] #定义列表用于存储40种攻击的条件熵
    #li = np.reshape(np.array(([-100]*40)*40),(40*40))
    #num = 0
    for num in range(0,40):
        i = 0  # i指第i列
        j = 0
        if num in counts.index: #如果num所代表的类存在数据,这一行的信息熵为计算值
            for i in range(0, 40):  # 计算这个类别下每个特征对应的信息熵，存储在列表liCon中
                liCon.append(compute(dta, i, num))  # 计算第i列针对类别j的信息熵，此时的liCon指的是一个列表，包含每个特征针对某一类别的信息熵
        else:   #如果num所代表的类中不存在数据，则这一行的信息熵为0
            for j in range(0,40):
                liCon.append(0)
    liCon = np.array(liCon).reshape((40,40))
    return liCon

if __name__ == "__main__":

  data = pd.read_csv("TsProcessedData.csv", sep=',',header=None)#选第一列
  Entropy = SeriHD(data)
  #Entropy = compute(data,0,1)
  print Entropy
  #for i, j in enumerate(Entropy):
   #   print i,j


