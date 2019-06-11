# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 02:32:11 2018

@author: Azumi Mamiya
"""
import numpy as np
import matplotlib.pyplot as plt

def main():
    alpha = 0.6
    beta=0.8
    hassei_t=[0.3,1.5,1.8,2.6,3.8,4.7,7.2,8.0,8.8]
    hassei_t=[0.28, 0.69, 0.76, 1.49, 1.75, 1.79, 2.03, 2.28, 2.36, 2.43, 2.43, 2.51, 2.52, 2.57, 2.76, 2.81, 2.82, 2.83, 2.87]
    x,y=[],[]
    
    for i in range(1000):
        t=i/100
        lam=1.2
        for ti in hassei_t:
            if  ti<t:
                lam += alpha*np.exp(-beta*(t-ti))
        x.append(t)
        y.append(lam)
    plot(x,y)

def plot(x,y):
    plt.plot(x,y,'-',markersize=1)
    
if __name__ == "__main__":
    main()