
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:44:53 2015
Calculates the difference among the daily
maximum temperature among the models

@author: BrianKim
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy
import AreaAvgOverTime
import GetDataMap

latRange = [5,20]
lonRange = [90,120]
models = ['bnu-esm', 'cnrm-cm5', 'ccsm4', 'noresm1-m']
# models = ['bnu-esm', 'cnrm-cm5']
avgOverTimeBaseNCEP = AreaAvgOverTime.AreaSumOverTime('tmax', ['ncep'], -1, [1985,2005], latRange, lonRange, 1, 11)
sums = []
for m in models:
	sums.append([m, AreaAvgOverTime.AreaSumOverTime('tasmax', [m], 1, [1985,2005], latRange, lonRange, 1, 11)])

meBase2, avgOverTimeFuture2)
bias = []
for s in sums:
	diff = [s[0], list()]
	for i in range(0, len(s[1][2])):
		diff[1].append(avgOverTimeBaseNCEP[2][i] - s[1][2][i])
	bias.append(diff)

fig = plt.figure()

for i in range(0, len(models)):
	avgOverTimeBase = avgOverTimeBaseNCEP
	tempDataLat = avgOverTimeBase[0]
	tempDataLon = avgOverTimeBase[1]
	tempDataData = bias[i][1]

	flatTLat = np.array(tempDataLat)
	flatTLon = np.array(tempDataLon)
	flatTData = np.array(tempDataData)
	# print flatTData
	y = flatTData
	N = len(y)
	x = range(N)
	width = 1/1.5

	height = float(1)/len(models)
	startHeight = i*height
	ax2 = fig.add_axes([.05, startHeight+.03, .9, height-.10])
	ax2.bar(x, y, width, color="blue")
	ax2.set_title("diff with " + str(bias[i][0]))

plt.ylabel('Precipitation (mm/day)')

plt.show()	