# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:28:53 2015

@author: claireyun
"""
import matplotlib.pyplot as plt

def FindHistogram(data):
    bins = range(170,310,5)
    tempHist = {}
    for i in data:
        for x in range(0,len(bins)-1):
            if not bins[x] in tempHist:
                tempHist[bins[x]] = 0
            if i >= bins[x] and i <= bins[x+1]:
                tempHist[bins[x]] += 1
    return tempHist
    
def PlotHistogram(data,min_bin,max_bin):
    plt.hist(data,bins=(range(min_bin,max_bin)),normed=True,cumulative=False)
    plt.show()
    
