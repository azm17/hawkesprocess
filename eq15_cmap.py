# -*- coding: utf-8 -*-
import numpy as np
import csv
from datetime import datetime
import matplotlib.pyplot as plt

x = np.linspace(0.01, 0.99, 99)
y = np.linspace(0.01, 0.99, 99)

X, Y = np.meshgrid(x, y)
Z = np.zeros((99,99))

def main():
    time_list=[0.3, 1.5, 1.8, 2.6, 3.8, 4.7, 7.2, 8.0, 8.8]
    #time_list=[e / 1000.0 for e in [0.3, 1.5, 1.8, 2.6, 3.8, 4.7, 7.2, 8.0, 8.8]]
    #time_list=[0.3, 1.5, 1.8, 1.9, 2.0, 2.1, 7.2, 8.0, 8.8]
    #tmp_time=read_time_csv('time1.csv')#発生時間のファイルを読み込み
    #time_list=[]
    #print(tmp_time[1])
    #for i in range(10):
    #    print(tmp_time[i])
    #    time_list.append(tmp_time[i])
    
    list2=['lnL','alpha','beta','lamda']
    saidai=fmax(time_list)
    for n in range(len(list2)):
        print(list2[n]+str(':'),saidai[n])
        
    plt.pcolormesh(X, Y, Z, cmap='inferno')
    plt.colorbar()
    plt.xlabel('$alpha$', fontsize=18)
    plt.ylabel('$beta$', fontsize=18)

def recursion(beta,t,i):
    if i == 0:
        return 0
    #elif i == 1:
    #    return np.exp(-beta*t[i]) * (1+recursion(beta,t,i-1))
    return np.exp(-beta*(t[i]-t[i-1])) * (1+recursion(beta,t,i-1))

def function(alpha,beta,lam,t):
    n=len(t)-1#n-1
    tmp1,tmp2,tmp3=0,0,0
    
    tmp1 = t[n]- lam*t[n]
    for i in range(n+1):#i:0->n
        tmp2 += alpha/beta*(1 - np.exp(-beta*(t[n] - t[i])))
    #R=0
    #tmp3 += np.log(lam + alpha*R)
    #for i in range(1,n+1):
    #    R = np.exp(-beta*(t[i]-t[i-1]))*(1+R)
    #   tmp3 += np.log(lam + alpha*R)
    for i in range(n+1):
        tmp3 += np.log(lam + alpha * recursion(beta,t,i))
    lnL=tmp1-tmp2+tmp3
    return lnL

def fmax(t):
    max_val,max_alpha,max_beta,lam_max=-100,0,0,0
    lam=1
    i = 0
    for beta in np.arange(0.01,1,0.01):
        j = 0
        for alpha in np.arange(0.01,1,0.01):
            #for lam in np.arange(0.01,2,0.01):
                tmp = function(alpha,beta,lam,t)
                Z[i, j] = tmp
                #print("{:2.1f} {:3.2f} {:3.2f} {:3.2f} {:3.2f}".format(tmp,max_val,max_alpha,max_beta,lam_max))
                if max_val < tmp:
                    max_val=tmp
                    max_alpha=alpha
                    max_beta=beta
                    lam_max=lam
                j += 1
        i += 1
    
    return [max_val,max_alpha,max_beta,lam_max]

def read_time_csv(filename):
    f = open(filename, 'r')
    time_list=[]#発生時間を格納
    reader = csv.reader(f)
    for row in reader:
        time_list.append(time_reform(row[0]))
    f.close()
    tmp=time_list[0]#スタート時間
    for j in range(len(time_list)):#すべての時間をスタート時間で引く
        time_list[j]-=tmp
    return time_list

def time_reform(str):#日付を秒に変換
    dt = datetime.strptime(str, '%Y/%m/%d %H:%M:%S')
    time=dt.day*60*60*24+dt.hour*60*60+dt.minute*60+dt.second
    return float(time)

if __name__ == "__main__":
    main()
