# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 2016
Calculates the difference among the daily
maximum temperature among the models for
each box on the grid

@author: BrianKim
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy
import AreaAvgOverTime
import GetDataMap
import DrawBaseMap


latRange = [5,20]
lonRange = [90,120]
# seasons from dec to february, march to may, june to august, sep to nov
monthStart = 9
monthEnd = 11
var1 = 'prate' #tmax for ncep
if var1 == 'tmax':
	var2 = 'tasmax'
elif var1 == 'prate':
	var2 = 'pr'
	
# models = ['csiro-mk3-6-0']
# models = ['bnu-esm']
models = ['hadgem2-es', 'bnu-esm', 'cnrm-cm5', 'ccsm4', 'noresm1-m'] #need tasmax

avgOverTimeBase = AreaAvgOverTime.AreaAvgOverTime(var1, ['ncep'], -1, [1985,2005], latRange, lonRange, monthStart, monthEnd)
sums = []
# for i in range(1, 11):
# 	print "ensemble: " + str(i)
# 	sums.append([str(i), AreaAvgOverTime.AreaAvgOverTime(var2, models, i, [1985,2005], latRange, lonRange, monthStart, monthEnd)])

for m in models:
	print m
	sums.append([m, AreaAvgOverTime.AreaAvgOverTime(var2, [m], 1, [1985,2005], latRange, lonRange, monthStart, monthEnd)])

bias = []
for s in sums:
	print s[0]
	diff = AreaAvgOverTime.AreaAvgDifference(avgOverTimeBase, s[1])
	bias.append(diff)

averageBias = []
for i in range(0, len(avgOverTimeBase[2])):
	row = []
	for j in range(0, len(avgOverTimeBase[2][0])):
		biasSum = 0
		for b in bias:
			biasSum += b[i][j]
		row.append(biasSum/len(bias))
	averageBias.append(row)

title =''
xlabel=''
minVal = -5
maxVal = 5

if var1 == 'prate':
	title = 'Bias of Precip Rate relative to NCEP Model in 1985-2005'
	xlabel = 'Precip (mm/day)'
	for i in range(0, len(averageBias)):
		for j in range(0, len(averageBias[0])):
			averageBias[i][j] *= 60*60*24
	minVal = -5
	maxVal = 5
elif var1 == 'tmax':
	title = 'Bias of Max Temperature relative to NCEP Model in 1985-2005'
	xlabel = 'Temperature (C)'


tempDataLat = avgOverTimeBase[0]
tempDataLon = avgOverTimeBase[1]
tempDataData = averageBias

flatTLat = np.array(tempDataLat)
flatTLon = np.array(tempDataLon)
flatTData = np.array(tempDataData)

print flatTData
print "Start Month: %d\n End Month: %d" % (monthStart, monthEnd)


DrawBaseMap.drawMap(flatTLon, flatTLat, flatTData, latRange, lonRange,
					 minVal, maxVal, title, xlabel)