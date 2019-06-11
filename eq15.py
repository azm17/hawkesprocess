# -*- coding: utf-8 -*-
import numpy as np
import csv
from datetime import datetime


def main():
    time_list=[0.3, 1.5, 1.8, 2.6, 3.8, 4.7, 7.2, 8.0, 8.8]
    time_list=[0.34, 2.5, 2.69, 2.86, 3.19, 3.73, 3.92, 4.03, 4.26, 4.28, 4.4, 4.51, 5.09, 5.1, 5.81, 5.84, 6.16, 6.48, 7.09, 7.17, 7.26, 7.3, 7.31, 7.9, 8.16, 8.41, 8.45, 8.52, 8.58, 9.13, 9.18, 9.27, 9.54, 9.59, 9.65, 9.71, 10.19, 10.2, 10.27, 10.9, 11.02, 11.14, 11.29, 11.48, 11.5, 11.57, 11.58, 11.67, 11.71, 12.08, 12.11, 12.26, 12.75, 13.21, 13.51, 13.53, 14.26, 14.27, 14.36, 14.46, 14.63, 14.75, 15.12, 15.21, 15.34, 15.4, 15.56, 15.59, 16.16, 16.52, 16.59, 16.64, 17.16, 17.4, 17.88, 18.67, 18.82, 19.94, 20.16, 20.97, 21.49, 21.52, 24.13, 25.89, 26.62, 26.78, 27.12, 27.45, 27.69, 28.27, 28.3, 28.3, 28.48, 28.49, 28.49, 28.52, 28.61, 28.63, 28.79, 28.93, 28.93, 28.93, 29.03, 29.06, 29.1, 29.26, 29.46, 29.59, 29.8, 29.84, 29.96, 30.02, 30.22, 30.53, 30.54, 30.85, 30.93, 31.0, 31.0, 31.29, 31.49, 31.62, 32.07, 32.87, 33.33, 33.39, 33.58, 33.73, 33.87, 34.33, 34.4, 34.52, 34.64, 34.96, 35.07, 35.68, 35.78, 35.85, 35.9, 35.94, 36.04, 36.33, 36.33, 36.41, 36.61, 36.77, 36.84, 36.96, 37.01, 37.01, 37.07, 37.28, 37.29, 37.87, 38.08, 38.09, 38.3, 38.39, 38.49, 38.65, 38.7, 38.71, 38.82, 39.06, 39.15, 39.48, 39.91, 40.2, 40.59, 40.6, 40.7, 40.8, 41.31, 41.72, 43.2, 43.39, 44.84, 44.93, 45.14, 45.47, 45.71, 45.9, 46.07, 46.08, 46.52, 47.01, 47.04, 47.55, 47.57, 47.61, 47.86, 47.89, 48.2, 48.55, 48.9, 49.1, 49.25, 49.83, 50.81, 54.79, 55.01, 55.26, 55.4, 55.63, 56.27, 56.47, 56.7, 56.75, 57.07, 57.08, 57.37, 57.63, 57.76, 57.79, 58.34, 58.51, 58.57, 59.52, 59.76, 59.93, 60.14, 60.26, 60.3, 60.46, 60.91, 60.93, 61.16, 61.34, 61.37, 61.37, 61.46, 61.51, 61.59, 61.67, 62.4, 62.43, 62.61, 62.81, 63.12, 63.19, 63.2, 63.29, 63.58, 63.61, 63.91, 63.91, 64.0, 64.13, 64.19, 64.22, 64.33, 64.38, 64.67, 64.69, 64.92, 65.03, 65.06, 65.1, 65.23, 65.34, 65.37, 66.12, 66.31, 66.46, 66.65, 66.69, 66.96, 67.29, 67.33, 67.48, 67.78, 67.95, 68.21, 68.35, 68.41, 68.48, 69.03, 69.08, 69.35, 69.44, 69.57, 69.73, 69.99, 70.01, 70.25, 70.48, 70.64, 70.85, 70.94, 71.42, 71.66, 71.71, 71.91, 72.0, 72.32, 73.24, 73.89, 74.29, 75.03, 75.82, 77.39, 77.46, 77.83, 78.98, 79.42, 79.54, 80.69, 81.25, 81.78, 82.87, 83.18, 83.48, 83.82, 84.72, 84.78, 84.94, 85.27, 85.7, 86.1, 86.46, 86.53, 86.58, 86.58, 86.66, 87.1, 89.04, 89.31, 89.33, 90.24, 90.71, 90.99, 91.38, 92.03, 92.05, 92.26, 92.31, 92.43, 92.88, 93.15, 93.15, 93.16, 93.21, 93.27, 93.56, 93.65, 93.77, 94.04, 94.04, 94.08, 94.17, 94.17, 94.19, 94.56, 94.58, 94.78, 94.94, 94.96, 95.03, 95.33, 95.49, 95.5, 95.56, 95.63, 95.73, 96.35, 96.39, 96.55, 96.58, 97.22, 97.25, 97.32, 97.33, 97.36, 97.74, 97.76, 97.98, 98.01, 98.06, 98.13, 98.21, 98.21, 98.44, 98.46, 98.48, 98.66, 98.76, 99.17, 99.2, 99.5, 99.52, 99.54, 99.78, 99.88, 99.93]
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
    #lam=1.2
    alpha = 0.6
    beta =0.8
    #for beta in np.arange(0.01,1,0.01):
        #for alpha in np.arange(0.01,1,0.01):
    for lam in np.arange(0.01,1.5,0.01):
        tmp = function(alpha,beta,lam,t)
        print("{:2.1f} {:3.2f} {:3.2f} {:3.2f} {:3.2f}".format(tmp,max_val,max_alpha,max_beta,lam_max))
        if max_val < tmp:
            max_val=tmp
            max_alpha=alpha
            max_beta=beta
            lam_max=lam
    
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