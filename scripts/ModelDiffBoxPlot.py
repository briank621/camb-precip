# -*- coding: utf-8 -*-
"""
Created on Aug 29, 2016

@author: Brian Kim
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy
import AreaAvgOverTime
import GetDataMap
import DrawBaseMap
import BoxPlot

latRange = [5,20]
lonRange = [90,120]
models = ['csiro-mk3-6-0']
# models = ['noresm1-m', 'cnrm-cm5', 'bnu-esm', 'ccsm4', 'hadgem2-es']
# models = ['noresm1-m', 'cnrm-cm5', 'bnu-esm']
var = 'pr'
# ensemble = [1]
ensemble = range(1, 11)
monthStart = 1
monthEnd = 12

baseOverTime = []
futOverTime = []
diffOverTime = []

for i in range(0, len(models)):
    for j in range(0, len(ensemble)):
    	baseOverTime = AreaAvgOverTime.AreaSumOverTime(var, [models[i]], 
    						[ensemble[j]], [1985,2005], latRange, lonRange, 
    						monthStart, monthEnd)
        futOverTime = AreaAvgOverTime.AreaSumOverTime(var, [models[i]], 
                            [ensemble[j]], [2045,2065], latRange, lonRange, 
                            monthStart, monthEnd)
        if(len(diffOverTime) == 0):
            diffOverTime = AreaAvgOverTime.SumAvgDifference(baseOverTime, futOverTime)
            for x in range(0, len(diffOverTime)):
                diffOverTime[x] = [diffOverTime[x]]
        else:
            diff = AreaAvgOverTime.SumAvgDifference(baseOverTime, futOverTime)
            for x in range(0, len(diffOverTime)):
                diffOverTime[x].append(diff[x])


print "diffTime: " + str(len(diffOverTime))
print "diffTime[0]: " + str(len(diffOverTime[0]))

for i in range(0,len(diffOverTime)):
    for j in range(0, len(diffOverTime[i])):
        diffOverTime[i][j]*=60*60*24


BoxPlot.draw(diffOverTime)

# plt.title('Difference in Precipitation in 2040-2060 Relative to 1985-2005')
plt.xlabel('Weeks of the Year')
plt.ylabel('Precip (mm/day)')

plt.show()


