#!/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

np.set_printoptions(suppress=True) #表示不以科学计数法输出
if __name__ == "__main__":
    #TrainData = np.loadtxt('KDDTrain.txt', delimiter=',')
   #TestData = np.loadtxt('KDDTest.txt', delimiter=',')
   #file = open("SimpleData.txt")
  data = pd.read_csv("E:/PythonBasis/TrProcessedData.csv", sep=',',header=None)
  #print data[40]
  # i = 0
  for i in range(0,41):
    if data[i].max() == 1:
        continue
    else:
        data[i] = (data[i]-data[i].min())/(data[i].max()-data[i].min())
  #data.to_csv('E:/PythonBasis/TrNormalizedData.csv',float_format = '%.2f', index = False, header = False)
  dn = data.values
  dn = dn[0:8000,0:41]
  dn = np.column_stack((dn, dn))
  dn = np.column_stack((dn,dn[0:,0:54]))
  print"Training data shape:", dn.shape
  print dn
  np.savetxt("Normailzed_DataSet.txt", dn, fmt='%.6f', delimiter=',')
  # df1 = pd.concat(data,df,left_index=True,right_index=)
  # print df1
    #print data[40].max()
  #print data.sha




