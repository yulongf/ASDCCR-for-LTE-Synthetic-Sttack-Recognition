#!/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd
import time
if __name__ == "__main__":
    print 'Loading data...'
    data = pd.read_csv("E:/PythonBasis/TrainData.txt", sep=',',header=None)
    str1 = ['tcp']
    str2 = ['ftp_data']
    str3 = ['SF']
    str41 = ['normal']
    i = 0
    time_start = time.time()
    print 'Start processing...'
    #定义
    while (1):
        if data.iloc[i,1] in str1:
            data.iloc[i, 1] = str1.index(data.iloc[i, 1])
        else:
            str1.append(data.iloc[i,1])
            data.iloc[i,1] = len(str1)

        if data.iloc[i,2] in str2:
            data.iloc[i, 2] = str2.index(data.iloc[i, 2])
        else:
            str2.append(data.iloc[i,2])
            data.iloc[i,2] = len(str2)

        if data.iloc[i,3] in str3:
            data.iloc[i, 3] = str3.index(data.iloc[i, 3])
        else:
            str3.append(data.iloc[i,3])
            data.iloc[i,3] = len(str3)

        if data.iloc[i,41] in str41:
            data.iloc[i, 41] = str41.index(data.iloc[i, 41])
        else:
            str1.append(data.iloc[i,41])
            data.iloc[i,41] = len(str41)

        i = i + 1
        if i >= len(data):
            break
    #print '数据类型为：', type(data)
    #print data
    time_end = time.time()
    print data.loc[0:5,0:42]
    print '时间消耗：', time_end - time_start, 's'
    #data.to_csv('F:/PythonDataLearning/PythonBasis/TrProcessedData.csv')

