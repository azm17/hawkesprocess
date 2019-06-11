import numpy as np
import matplotlib.pyplot as plt
import csv
from datetime import datetime

def main():
    time_list=read_time_csv('time1.csv')#発生時間のファイルを読み込み
    #print(time_list)
    tmax=400#最大時間
    alpha=0.2
    beta=0.09
    x,y=[],[]#x,y
    for t in range(int(tmax)):
        lam=0.1
        for ti in time_list:
            if  ti<t:
                lam += alpha*np.exp(-beta*(t-ti))
        x.append(t)#x座標　
        y.append(lam)#y座標
    plot(x,y)#グラフ作成

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
    
def plot(x,y):#プロットするだけ
    plt.plot(x,y,'-',markersize=1)
    
if __name__ == "__main__":
    main()