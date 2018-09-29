# -*- coding: utf-8 -*-
"""
Created on Mon May  7 08:12:43 2018

@author: Eimon
"""

import numpy as np
import  math
import random

l1=[[0,0,0,0,0,0,1,1,1,1,1,1],
    [0,0,0,0,1,1,0,0,0,0,1,1],
    [0,0,1,1,0,0,0,0,1,1,0,0,],
    [0,1,0,1,0,1,0,1,0,1,0,1]]

I=np.array(l1) 

l2 = [[1,-1,0.1,0.5],[0.9,0.5,1,-0.7],[0.5,0.6,0.8,0.2],[0.5,-0.1,0.6,0.4]]

In_to_H=np.array(l2)

l3 = [[0.9,1,0.3,0.5],[1,0.4,-0.2,-0.7]]

H_to_out=np.array(l3)

l4= [[0,1,1,0,1,0,1,0,0,1,0,1],
     [0,0,0,0,1,1,1,1,0,0,0,0]]

Target=np.array(l4)

def sigmoid(z):
    
    n = np.shape(z)
    temp = np.ones((n[0],n[1]))
    
    i = 0
    j = 0
    
    while(i<n[0]):
        j=0
        while(j<n[1]):
            temp[i][j] = 1 / (1 + math.exp(-z[i][j]))
            j = j+1
        i=i+1
        
    return temp



Z_H=np.dot(In_to_H,I) 
Y_H=sigmoid(Z_H)

Z_O=np.dot(H_to_out,Y_H) 
Y_O=sigmoid(Z_O)

lam_JK=(Target-Y_O)*(Y_O)*(1-Y_O)

delta_HO=np.dot(lam_JK,Y_H.T)

lam_IJ=((np.dot(lam_JK.T,H_to_out)).T)*(Y_H)*(1-Y_H)

delta_IH=np.dot(lam_IJ,I.T)

rate=2

In_to_H=In_to_H+(rate*delta_IH)

H_to_out=H_to_out+(rate*delta_HO)
























