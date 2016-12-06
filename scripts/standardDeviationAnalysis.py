# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:05:31 2015

@author: claireyun
"""

import GetDataMap
import Histogram
import LoadDataYear
import LatLonIndex
import numpy
import matplotlib.pyplot as plt

def stdAnalysis():
    latLonRange = LatLonIndex.findLatLonRange([26,32] , [80,88], [])
    standardDev = []
    for i in range(1994,2005,1):
        m = GetDataMap.getDataMap(latLonRange[0], latLonRange[1], i, 'pr')
        for j in range(0,m[2]):
            for m in range(0,len(m[2])):
                for n in range(0,len(m[2][0])):
                    for n in range(0,len(m[2][0][0])):
                        #do something
        #g = GetDataMap.getAreaAvg(m)
        #del m
        standardDev.append(numpy.std(g))
        #del g
        print i 
    
    plt.plot(standardDev)

stdAnalysis()