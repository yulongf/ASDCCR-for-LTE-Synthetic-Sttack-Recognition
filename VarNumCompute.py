#!/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt


def Varnum(x):
    vs = 0
    AvgNum = sum(x)/len(x)
    #print AvgNum
    for i in range(len(x)):
        vs = vs + np.square(x[i]-AvgNum)
    return vs/len(x)


if __name__ == '__main__':
    a = np.loadtxt('E:/PythonBasis/IG_DataSet.txt',delimiter = ',')
    #b = np.empty([2, 40], dtype=float)  # 表示定义一个2*2的矩阵，该矩阵为整型

    print 'Information Gain shape:', a.shape

    b = [0]
    for i in range(0,4):
        if i==0:
            b[i] = Varnum(a[i])
        else:
           b.append(Varnum(a[i]))
    x = range(0,4)
    #plt.figure()
    plt.figure(facecolor='w')
    plt.plot(x,b,color="red", linewidth=2)
    plt.xlabel("Classes")
    plt.ylabel("Variance")
    plt.title("Variance for classes")
    plt.show()
    np.set_printoptions(linewidth=10, suppress=True)
    print b

    print len(b)