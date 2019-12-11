#!/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd
import time
if __name__ == "__main__":
    data = pd.read_csv("KDDTest.txt", sep=',',header=None)
    str1 = ['tcp', 'icmp', 'udp']
    str2 = ['aol', 'auth', 'bgp', 'courier', 'csnet_ns', 'ctf', 'daytime', 'discard', 'domain', 'domain_u', \
            'echo', 'eco_i', 'ecr_i', 'efs', 'exec', 'finger', 'ftp', 'ftp_data', 'gopher', 'harvest', \
            'hostnames', 'http', 'http_2784', 'http_443', 'http_8001', 'imap4', 'IRC', 'iso_tsap', 'klogin',  \
            'kshell', 'ldap', 'link', 'login', 'mtp', 'name', 'netbios_dgm', 'netbios_ns', 'netbios_ssn', \
            'netstat', 'nnsp', 'nntp', 'ntp_u', 'other', 'pm_dump', 'pop_2', 'pop_3', 'printer', 'private', \
            'red_i', 'remote_job', 'rje', 'shell', 'smtp', 'sql_net', 'ssh', 'sunrpc', 'supdup', 'systat', \
            'telnet', 'tftp_u', 'tim_i', 'time', 'urh_i', 'urp_i', 'uucp', 'uucp_path', 'vmnet', \
            'whois', 'X11', 'Z39_50']
    str3 = ['OTH', 'REJ', 'RSTO', 'RSTOS0', 'RSTR', 'S0', 'S1', 'S2', 'S3', 'SF', 'SH']
    str42 = ['normal', 'ipsweep', 'mscan', 'nmap', 'portsweep', 'saint', 'satan', \
             'apache2', 'back' ,'land', 'mailbomb', 'neptune', 'pod', 'processtable', \
             'smurf', 'teardrop', 'udpstorm', 'buffer_overflow', 'httptunnel', 'loadmodule', 'perl', \
             'ps', 'rootkit', 'sqlattack', 'xterm', 'ftp_write', 'guess_passwd', 'imap', 'multihop', \
             'named', 'phf', 'sendmail', 'snmpgetattack', 'spy', 'warezclient', 'warezmaster', 'worm', \
             'xlock', 'xsnoop', 'snmpguess']
    i = 0

    time_start = time.time()
    #定义
    while (1):
        data.iloc[i,1] = str1.index(data.iloc[i,1])
        data.iloc[i,2] = str2.index(data.iloc[i,2])
        data.iloc[i,3] = str3.index(data.iloc[i,3])
        data.iloc[i,41] = str42.index(data.iloc[i,41])
        i = i + 1
        if i >= len(data):
            break
    #print '数据类型为：', type(data)
    #print data
    time_end = time.time()
    print data.loc[0:5,0:42]
    print '时间消耗：', time_end-time_start, 's'
    data.to_csv('E:/PythonBasis/TsProcessedData.csv',index = False, header = False)

