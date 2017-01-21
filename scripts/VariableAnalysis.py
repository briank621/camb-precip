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
import DrawBaseMap

latRange = [5,20]
lonRange = [90,120]
# models = ['csiro-mk3-6-0']
models = ['noresm1-m', 'cnrm-cm5', 'bnu-esm', 'ccsm4']
# var = 'tasmax'
var = 'pr'
ensemble = [1]
# ensemble = range(1, 11)
# monthsStart = [12, 3, 6, 9]
monthsStart = [1]
monthsEnd = [12]
# monthsEnd = [2, 5, 8, 11]
#seasons from dec to february, march to may, june to august, sep to nov
for s in range(0, len(monthsStart)):
	monthStart = monthsStart[s]
	monthEnd = monthsEnd[s]
	avgOverTimeBase = AreaAvgOverTime.AreaAvgOverTime(var, models, ensemble, [1985,2005], latRange, lonRange, monthStart, monthEnd)
	avgOverTimeFuture = AreaAvgOverTime.AreaAvgOverTime(var,models, ensemble, [2045,2065], latRange, lonRange, monthStart, monthEnd)

	avgOverTime = AreaAvgOverTime.AreaAvgDifference(avgOverTimeBase, avgOverTimeFuture)
	if var == 'pr':
		for i in range(0,len(avgOverTime)):
		    for j in range(0,len(avgOverTime[i])):
		        avgOverTime[i][j]*=60*60*24

	tempDataLat = avgOverTimeBase[0]
	tempDataLon = avgOverTimeBase[1]
	tempDataData = avgOverTime

	flatTLat = np.array(tempDataLat)
	flatTLon = np.array(tempDataLon)
	flatTData = np.array(tempDataData)
	print flatTData

	if var == 'pr':
		minVal = -.5
		maxVal = .5
		title = 'Mean Precipitation in 2045-2065 Relative to 1985-2005 '
		xlabel = 'Precipitation (mm/day) for Months (%d, %d)' % (monthStart, monthEnd)
	else:
		minVal = -5
		maxVal = 5
		title = 'Mean Max Temp in 2045-2065 Relative to 1985-2005 '
		xlabel = 'Temperature for Months (%d, %d)' % (monthStart, monthEnd)

	plt.figure()
	DrawBaseMap.drawMap(flatTLon, flatTLat, flatTData, latRange, lonRange,
						 minVal, maxVal, title, xlabel, "avgPrecipMapModels.eps", False)

# plt.show()

#PRINTS OUT ALL THE INDIVIDUAL MODELS ONE AT A TIME
# for m in models:
# 	print m
# 	for s in range(0, len(monthsStart)):
# 		monthStart = monthsStart[s]
# 		monthEnd = monthsEnd[s]
# 		avgOverTimeBase = AreaAvgOverTime.AreaAvgOverTime(var, [m], ensemble, [1985,2005], latRange, lonRange, monthStart, monthEnd)
# 		avgOverTimeFuture = AreaAvgOverTime.AreaAvgOverTime(var,[m], ensemble, [2045,2065], latRange, lonRange, monthStart, monthEnd)

# 		avgOverTime = AreaAvgOverTime.AreaAvgDifference(avgOverTimeBase, avgOverTimeFuture)
		
# 		for i in range(0,len(avgOverTime)):
# 		    for j in range(0,len(avgOverTime[i])):
# 		        avgOverTime[i][j]*=60*60*24

# 		tempDataLat = avgOverTimeBase[0]
# 		tempDataLon = avgOverTimeBase[1]
# 		tempDataData = avgOverTime

# 		flatTLat = np.array(tempDataLat)
# 		flatTLon = np.array(tempDataLon)
# 		flatTData = np.array(tempDataData)
# 		print flatTData

# 		minVal = -.5
# 		maxVal = .5

# 		plt.figure()
# 		title = ""
# 		title = 'Daily Precipitation in 2040-2060 Relative to 1985-2005 '
# 		xlabel = 'Precipitation (mm/day)'
# 		# xlabel = 'Difference in Max Temperature (C)'
# 		# xlabel = 'Difference in Max Temperature (C) for model: ' + m
# 		DrawBaseMap.drawMap(flatTLon, flatTLat, flatTData, latRange, lonRange,
# 							 minVal, maxVal, title, xlabel, "avgPrecipMapModels.eps", False)

plt.show()



