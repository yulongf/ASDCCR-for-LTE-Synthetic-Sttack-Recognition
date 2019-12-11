#!/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd
import math
import numpy as np

###信息熵计算过程
np.set_printoptions(suppress=True) #表示不以科学计数法输出
#计算类别的信息熵
def IG_DP (c, t, i):
    HD = -float(c[i]/t)* math.log(float(c[i])/t,2)-(float(t-c[i])/t)* math.log(float(t-c[i])/t,2)
    return HD

def IG_Dk (d):
    counts = d[41].value_counts()  #
    total = sum(counts)
    listHD = [0]  #
    listHD = listHD * 40
    i = 0

    # while循环用于计算40个数据类别的信息熵
    while (1):
        if i in counts.index:
            listHD[i] = IG_DP(counts, total, i)
        else:
            listHD[i] = -0.5  #
        i = i + 1
        if i >= 40:
            break
    return listHD

#计算某一列某个范围内的条件熵
def HD0 (da,x,y,z,w): #参数为data，即原始数据集,x为范围选择下限，y为范围选择上限，z为列的特征属性,w为类别标签
    D0 = da[[z, 41]][(da[z] >= x) & (da[z] < y)]  #得到第一列0到0.1之间的数和对应的类别标签列
    F0 = D0[z][(D0[41]==w)] #得到0到0.1之间类别标签为0的数
    total, d, f = len(da), len(D0), len(F0) #total指数据集总条数，d指数据集中0到0.1的条目，f指0到0.1数据中类别为0的数据条目
    #print total, d, f
    if d-f == 0 or d == 0 or f == 0:
        HD = 0
    else:
        HD = (float(d)/total)*((-float(f)/d)*math.log(float(f)/d,2)-float((d-f)/d)*math.log(float(d-f)/d,2))
    return HD

#计算b类a列的条件熵
def compute (dt,a,b):#第b个类别的第a个特征属性
    #tha = 100.0
    i = 0.0
    D = 0.0
    j = 0
    #print
    while (1):
        D = D + HD0(dt, i, i + 0.01,a,b)
        i = i + 0.1
        j = j + 1
        if j >= 1:
            break
    return D

#计算类0的条件熵列表，即正常数据
def SeriHD (dta):
    counts = dta[41].value_counts() #原始数据集每个类别的记录
    liCon = [] #定义列表用于存储40种攻击的条件熵
    #li = np.reshape(np.array(([-100]*40)*40),(40*40))
    #num = 0
    for num in range(0,40):
        i = 0  # i指第i列
        j = 0
        if num in counts.index: #如果num所代表的类存在数据,这一行的信息熵为计算值
            for i in range(0, 41):  # 计算这个类别下每个特征对应的信息熵，存储在列表liCon中
                liCon.append(compute(dta, i, num))  # 计算第i列针对类别j的信息熵，此时的liCon指的是一个列表，包含每个特征针对某一类别的信息熵
        else:   #如果num所代表的类中不存在数据，则这一行的信息熵为0
            for j in range(0,41):
                liCon.append(0)
    liCon = np.array(liCon).reshape((40,41))
    return liCon

if __name__ == "__main__":
  data = pd.read_csv("E:/PythonBasis/TrNormalizedData.csv", sep=',',header=None)
  #print data[41]
  HD = IG_Dk(data) #写成矩阵转置的形式
  HDA = np.array(HD).reshape(40,1)
  HDA = np.tile(HDA,(1,41))#将转置后的矩阵在列方向上重复40次
  Entropy = SeriHD(data)
  IG = HDA - Entropy+0.4
  IG_data = IG[0:4,0:]
  IG_data = np.column_stack((IG_data ,IG_data))
  IG_data = np.column_stack((IG_data, IG_data[0:,0:54]))
  R = np.random.random((4,136))*0.5
  #print R.shape
  IG_data = IG_data - R
  #IG_data = np.column_stack((IG_data,IG_data[0:,0:17]))
  # for i in range(4,len(IG)):
  #     np.delete(IG, i, axis = 0)
  #HDA = np.reshape(np.array(HD*40),(40,40))
  np.savetxt("IG_DataSet.txt",IG_data, fmt = '%.6f', delimiter = ',')
  print 'Information Gain shape:', IG_data.shape
  print 'Inmormation Gain:\n', IG_data
  #HDA = np.reshape(np.)

  #计算g(D_0;f_1)
  #for i, j in enumerate(HD):
   #   print i,j


