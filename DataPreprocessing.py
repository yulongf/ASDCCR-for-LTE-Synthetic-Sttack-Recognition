#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

if __name__ == "__main__":
    #TrainData = np.loadtxt('KDDTrain.txt', delimiter=',')
   #TestData = np.loadtxt('KDDTest.txt', delimiter=',')
   #file = open("SimpleData.txt")
  data = pd.read_csv("TrainData.txt", sep=',',header=None)
  #data.columus = ['Duration','Protocol_type','Service','Flag','Src_bytes','Dst_bytes']
  print 'Start preprocessing...'
  i = 0
  while(1):
      if data.iloc[i,1] == 'tcp':  #先处理第一列，有三种
         data.iloc[i, 1] = 0  # 第0行第1列
      elif data.iloc[i,1] == 'icmp':
          data.iloc[i,1] =1
      elif data.iloc[i,1] == 'udp':
          data.iloc[i,1] = 1

      i = i+1
      if i >=len(data):
          break
  print data
  #data[1] = data[1].astype('int')

  i = 0
  while(1):
       if data[1][i] == 'tcp':
        data[1][i] = 0
       i = i+1
       if i>=5:
           break
  #data.to_csv('F:/PythonDataLearning/PythonBasis/prediction.csv')
  print data



