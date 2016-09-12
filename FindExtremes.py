# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 13:21:30 2015

@author: claireyun
"""
import GetDataMap
import LoadDataYear
import sys

def findAnnualMax(data):
    highestTemps = []
    for i in range(0,len(data)):
        row = []
        for j in range(0, len(data[i])):
            row.append(sys.maxint)
        highestTemps.append(row)
    
    for i in range(0,len(data)):
        for j in range(0, len(data[i])):
            for t in range(0, len(data[i][j])):
                if highestTemps[i][j] == sys.maxint or data[i][j][t] > highestTemps[i][j]:
                    highestTemps[i][j] = data[i][j][t]
    
    return highestTemps
    
