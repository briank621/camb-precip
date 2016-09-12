# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:44:53 2015

@author: JackieRyu
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy
import AreaAvgOverTime
import GetDataMap

latRange = [5,20]
lonRange = [90,120]
# models = ['csiro-mk3-6-0']
models = ['noresm1-m', 'cnrm-cm5', 'bnu-esm', 'ccsm4', 'hadgem2-es']
var = 'pr'
ensemble = [1]
# ensemble = range(1, 11)
monthStart = 1
monthEnd = 12
# monthsStart = [12, 3, 6, 9]
# monthsEnd = [2, 5, 8, 11]

for m in models:
	print m
	sumOverTimeBase = AreaAvgOverTime.AreaSumOverTime(var, [m], ensemble, [1985,2005], latRange, lonRange, monthStart, monthEnd)
	sumOverTimeFuture = AreaAvgOverTime.AreaSumOverTime(var, [m], ensemble, [2045,2065], latRange, lonRange, monthStart, monthEnd)

	if var == 'pr':
		for i in range(0,len(sumOverTimeFuture[2])):
			sumOverTimeBase[2][i]*=60*60*24
			sumOverTimeFuture[2][i]*=60*60*24

	# print str(sumOverTimeBase)

	tempDataLat = sumOverTimeFuture[0]
	tempDataLon = sumOverTimeFuture[1]
	# tempDataData = sumOverTimeFuture[2]
	tempDataData = AreaAvgOverTime.SumAvgDifference(sumOverTimeBase, sumOverTimeFuture)

	flatTLat = np.array(tempDataLat)
	flatTLon = np.array(tempDataLon)
	flatTData = np.array(tempDataData)
	print flatTData

	y = flatTData
	N = len(y)
	x = range(N)
	width = 1/1.5
	plt.figure()
	plt.bar(x, y, width, color="blue")

	# Add Title
	# plt.title('Weekly Precipitation in Cambodia From 1985-2005  ')
	plt.title('Difference Weekly Precipitation in Cambodia From 2045-2065 To 1985-2005  ')
	plt.xlabel('Weeks of the Year for model: ' + m)
# plt.ylabel('Precipitation (mm/day)')

plt.show()