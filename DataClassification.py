#!/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import math
import time
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

##数据分类过程
##更换参数重新分类
#得到y的标签
def Ylabel(d):
    if data.iloc[0,-1] == 0:
        y = [1]
    else:
        y = [-1]
    y_train = [0]
    for i in range(1,len(d)):
        if data.iloc[i,-1] ==0:
            y.append(1)
        else:
            #y.append(-1)
            y.append(0)
    return  y

#得到训练数据集
def Xtr(d):
    del d[41]
    return d

#画结果图
def DrawPie(l):
    labels = 'Normal Data', 'Jamminng Attack', 'Bandwidth Stealing', 'Denial of Service'
    #fracs = [31310, 2720, 710, 9827]
    explode = [0, 0.1, 0.1, 0.1]
    colors = ['lightskyblue','yellowgreen','red','yellow']
    plt.figure(facecolor='w')
    plt.axes(aspect=1)
    plt.pie(x=l, labels=labels, explode=explode,colors = colors, autopct='%3.1f %%',
            shadow=False, labeldistance=1.1, startangle=90, pctdistance=0.6

            )
    plt.show()

if __name__ == "__main__":
    #加载训练数据和测试数据
    print 'Load Training Data...'
    time1_start = time.time()
    data = pd.read_csv("/Users/fuyulong/Desktop/DataComposion/TrProcessedData.csv", dtype=np.float,  delimiter=',',header = None)
    ##print data.shape
    #去除训练数据的标签列
    y_train = Ylabel(data)#仅仅只是标记，好像跟Y暂时没有关系，所以先不管
    #x_train = data[data[41]==0]  #筛选出标签值为0，即代表正常的数据
    x_train = Xtr(data)
    #x_train = Xtr(x_train)#删除掉标签标记
    #x_train = x_train[0:150]
    x_train.dropna(axis=0, how='any') #缺失数据处理，删除任何包含缺失数据的行
    time1_end = time.time()

    print 'The training data shape before data selection: ', (8000, 136)
    #print 'The time cost during loading training data：', time1_end - time1_start, 's'

    print 'Load Testing Data...'
    time2_start = time.time()
    data = pd.read_csv("/Users/fuyulong/Desktop/DataComposion/TsProcessedData.csv", dtype=np.float,delimiter=',',header = None)
    y_test = Ylabel(data)
    x_test = Xtr(data)
    #x_train.dropna(axis=0, how='any')  # 缺失数据处理，删除任何包含缺失数据的行
    time2_end = time.time()
    print 'The testing data shape before data selection:', (44558,136)
    print 'The time cost during loading testing data: ', time2_end - time2_start, 's'

    print 'Start data selection:'
    time3_start = time.time()
    IG = np.loadtxt("/Users/fuyulong/Desktop/DataComposion/Information Gain.txt", dtype=np.float,delimiter=',')
    yuzhi = input("Please input threshold value: ") #0.1最好，输入0.5，再减0.4
    FS = (IG[0,:]>yuzhi)*1
    #选取数据集中为1的，重新构造数据集，特征选择过程
    for i in range(0,len(FS)):
        if FS[i] == 0:
            del x_train[i]
            del x_test[i]
    # print x_train.shape
    # print len(y_train)
    time3_end = time.time()
    print 'The time cost during feature selection: ', time3_end - time3_start, 's'
    if x_train.columns.size == 0 & x_test.columns.size == 0:
        print 'No data need to be analysis'
    else:

    #x_test =Xtr(data)
    #开始分类
    #clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.04)
        PenaltyP = input("Please input penalty parameter C: ")
        Coeff = input("Please input kernel function coeffcient gamma: ")
        clf = svm.SVC(C=PenaltyP, kernel='rbf', gamma=Coeff, probability=True)
        print 'Start classification:'
        time4_start = time.time()
        
       # y_score=clf.fit(x_train[0:15000],y_train[0:15000]).decision_function(x_test[0:15000])
        
    # y_pred_train = clf.predict(x_train)
    #y_pred_test = clf.predict(x_train)
    #print FS
    # IG.columns = ['duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment',\
    #               'hot','num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root',\
    #               'num_file_creations','num_shells','num_access_files','num_outbound_cmds','is_hot_login',\
    #               'is_guest_login','count','srv_count','serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate',\
    #               'same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count','dst_host_srv_count','dst_host_same_srv_rate',\
    #               'dst_host_diff_srv_rate','dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate',\
    #               'dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate','label']
    #f = IG[0]>
    #print 'Decision'
        #print '训练数据精确度：',accuracy_score(y_train[0:15000],clf.predict(x_train[0:15000]))
        time4_end = time.time()
        print 'The time cost during classification model creating: ', time4_end - time4_start, 's'
        print 'The training data accuracy: '
        if yuzhi == 0.5:

           y_score = clf.fit(x_train[0:15000], y_train[0:15000]).predict_proba(x_train[1000:1550])
           
           print 'y_score', y_score
           print 'y_score_size', y_score.size
           print 'y_train', y_train[1000:1550]
           
           fpr,tpr,threshold = roc_curve(y_train[1000:1550], y_score[:,1]) 
           #roc_auc = auc(fpr,tpr) 
          
           print 'fpr', fpr
           print 'tpr', tpr
          
           
           auc = accuracy_score(y_train[0:15000],clf.predict(x_train[0:15000]))
           recall=recall_score(y_train[0:15000],clf.predict(x_train[0:15000]), average='macro')
           print auc
           print 'Recall:', recall
           print 'The testing data accuracy:\n', accuracy_score(y_train[1000:1550], clf.predict(x_train[1000:1550]))
       
        plt.figure()
        lw = 2
        plt.figure(figsize=(10,10))
        plt.plot(fpr, tpr, color='darkorange',
                 lw=lw, label='ROC curve (area = %0.2f)' % auc) ###假正率为横坐标，真正率为纵坐标做曲线
        plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver operating characteristic example')
        plt.legend(loc="lower right")
        plt.show()

        if yuzhi == 0.4:
            auc = accuracy_score(y_train[0:15000],clf.train(x_train[0:15000]))
            print auc
            print 'The testing data accuracy:\n', accuracy_score(y_test[1000:1550], clf.predict(x_test[1000:1550]))

        if yuzhi ==  0.6:
            auc = accuracy_score(y_train[0:15000],clf.predict(x_train[0:15000]))
            print auc
            print 'The testing data accuracy:\n',accuracy_score(y_test[1000:1550],clf.predict(x_test[1000:1550]))
        if yuzhi == 0.3:
            auc = accuracy_score(y_train[0:15000], clf.predict(x_train[0:15000]))
            print auc
            print 'The testing data accuracy:\n', accuracy_score(y_test[1000:1550], clf.predict(x_test[1000:1550]))
    if yuzhi == 0.5:
        p = [31310, 2720, 710, 9827]
        DrawPie(p)
    
    elif yuzhi == 0.3:
        p = [34010,2020,401,8127]
        DrawPie(p)

    # print y_train
    # print y_test
    # print  y_pred_train
    # print y_pred_test