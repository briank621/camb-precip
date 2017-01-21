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

avgOverTime = []
sumOverTime = []

for i in range(0, len(models)):
    for j in range(0, len(ensemble)):
    	if(len(sumOverTime) == 0):
        	sumOverTime = AreaAvgOverTime.AreaSumOverTime(var, [models[i]], 
        						[ensemble[j]], [2045,2065], latRange, lonRange, 
        						monthStart, monthEnd)
        	for x in range(0, len(sumOverTime[2])):
        		sumOverTime[2][x] = [sumOverTime[2][x]]
        else:
			nextModel = AreaAvgOverTime.AreaSumOverTime(var, [models[i]], 
						[ensemble[j]], [2045,2065], latRange, lonRange, 
						monthStart, monthEnd)
			print "len: " + str(len(sumOverTime))
			print "len: " + str(len(sumOverTime[2]))
			for x in range(0, len(sumOverTime[2])):
				sumOverTime[2][x].append(nextModel[2][x])


for i in range(0,len(sumOverTime[2])):
	for j in range(0, len(sumOverTime[2][0])):
   		sumOverTime[2][i][j]*=60*60*24

path = "data/plots/high_res/futureboxplot.eps"
BoxPlot.draw(sumOverTime[2])

plt.title('Weekly Precipitation in Cambodia from 2045-2065')
plt.xlabel('Weeks of the Year')
plt.ylabel('Precip (mm/day)')

fig = plt.gcf()
fig.set_size_inches(16, 9)

plt.savefig(path, format='eps', dpi=1000)
plt.show()

