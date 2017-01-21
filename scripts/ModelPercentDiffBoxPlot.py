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
# ensemble = [1, 2]
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

avgOverTime = []
sumOverTime = []

for i in range(0, len(models)):
    for j in range(0, len(ensemble)):
        if(len(sumOverTime) == 0):
            sumOverTime = AreaAvgOverTime.AreaSumOverTime(var, [models[i]], 
                                [ensemble[j]], [1985,2005], latRange, lonRange, 
                                monthStart, monthEnd)
            for x in range(0, len(sumOverTime[2])):
                sumOverTime[2][x] = [sumOverTime[2][x]]
        else:
            nextModel = AreaAvgOverTime.AreaSumOverTime(var, [models[i]], 
                        [ensemble[j]], [1985,2005], latRange, lonRange, 
                        monthStart, monthEnd)
            print "len: " + str(len(sumOverTime))
            print "len: " + str(len(sumOverTime[2]))
            for x in range(0, len(sumOverTime[2])):
                sumOverTime[2][x].append(nextModel[2][x])


for i in range(0,len(sumOverTime[2])):
    for j in range(0, len(sumOverTime[2][0])):
        sumOverTime[2][i][j]*=60*60*24

avgPast = []
percentDiff = []

for i in range(0,len(sumOverTime[2])):
    avg = 0
    for j in range(0, len(sumOverTime[2][i])):
        avg += sumOverTime[2][i][j]
    avg /= len(sumOverTime[2][i])
    avgPast.append(avg)

percentDiff = []

for i in range(0, len(diffOverTime)):
    percents = []
    for j in range(0, len(diffOverTime[i])):
        p = (diffOverTime[i][j])/(avgPast[i])
        p *= 100
        percents.append(p)
    percentDiff.append(percents)


path = "data/plots/high_res/percentboxplot.eps"
BoxPlot.draw(percentDiff)

plt.title('Percentage Difference in Precipitation in 2040-2060 Relative to 1985-2005')
plt.xlabel('Weeks of the Year')
plt.ylabel('Percent Difference')

fig = plt.gcf()
fig.set_size_inches(16, 9)

plt.savefig(path, format='eps', dpi=1000)
plt.show()


