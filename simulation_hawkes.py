# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:21:30 2018

@author: azm
"""
import random
import numpy as np
import matplotlib.pyplot as plt

lam_0 = 1.2
alpha = 0.6
beta = 0.8
T = 100
  
def simulation():
    t=[]
    lam_star = lam_0
    n = 0
    u = random.random()#U[0,1]
    s = - 1/lam_star * np.log(u)
    t.append(float('{:2.2f}'.format(s)))#t <- s
    
    while(True):
        n = n + 1
        lam_star = lam_func(t[n-1],t) + alpha
        while(True):
            #--New event--
            u = random.random()#U[0,1]
            s = s - 1/lam_star * np.log(u)
            if s >= T:
                break
            #--Rejection test--
            D = random.random()#U[0,1]
            if D <= lam_func(s,t)/lam_star:
                t.append(float('{:2.2f}'.format(s)))#t <- s
                break
            else:
                lam_star = lam_func(s,t)
        if s >= T:
            break
    return t

def lam_func(t,hassei_t):
    lam = lam_0
    for ti in hassei_t:
            if  ti < t:
                lam += alpha*np.exp(-beta*(t-ti))
    return lam

def main(hassei_t):
    #hassei_t=[0.3,1.5,1.8,2.6,3.8,4.7,7.2,8.0,8.8]
    #hassei_t=[0.28, 0.69, 0.76, 1.49, 1.75, 1.79, 2.03, 2.28, 2.36, 2.43, 2.43, 2.51, 2.52, 2.57, 2.76, 2.81, 2.82, 2.83, 2.87]
    x,y=[],[]
    print(hassei_t)
    for i in range(100):
        t=i/10
        lam = lam_0
        for ti in hassei_t:
            if  ti<t:
                lam += alpha*np.exp(-beta*(t-ti))
        x.append(t)
        y.append(lam)
    plot(x,y)
        
        
    
def plot(x,y):#プロットするだけ
    plt.plot(x,y,'-',markersize=1)
    
if __name__ == "__main__":
    t=simulation()
    main(t)