# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:58:46 2015

@author: claireyun
"""
import sys

def percentile(data, percentage):
    data.sort()
    return data[int(percentage/100.0 *len(data))]

def AnnualMax(data):
    x = sys.maxint
    for i in range(len(data)):
        if i > x or x == sys.maxint:
            x = data[i]
    return x
    
def AnnualMin(data):
    y = sys.maxint
    for j in range(len(data)):
        if j < y or y == sys.maxint:
            y = data[j]
    return y