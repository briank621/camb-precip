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

latRange = [13,15]
lonRange = [106,108]

# latRange = [5,20]
# lonRange = [90,120]
models = ['csiro-mk3-6-0']
# models = ['noresm1-m', 'cnrm-cm5', 'bnu-esm', 'ccsm4', 'hadgem2-es']
# models = ['noresm1-m']
var = 'pr'
# ensemble = [1]
years = range(1985, 2005)
ensemble = range(1, 11)
# monthsStart = [12, 3, 6, 9]
dayStart = 0
dayEnd = 328
precip = []
durations = []

for m in models:
	print m
	durations = []
	for e in ensemble:
		print "Ensemble: " + str(e)
		for y in years:
			# print y
			g = GetDataMap.getDataMap(latRange, lonRange, y, m, e, var)
			#print "g[2] Length: " + str(len(g[2]))
			#print "g[2][0] Length: " + str(len(g[2][0]))
			for i in range(len(g[2])):
				for j in range(len(g[2][i])):
					consec = 0
					for d in range(dayStart, dayEnd):
						val = g[2][i][j][d]*60*60*24
						if(val < 10):
							consec += 1
						elif consec > 0:
							#print consec
							durations.append(consec)
							consec = 0

	plt.figure()
	plt.hist(durations, bins=range(0, 25))
	plt.title("Histogram of Duration of Dry Days (%s)" % (m))
	plt.xlabel('Number of Consecutive Days')
	plt.ylabel('Frequency')

plt.show()

	# print str(np.percentile(durations, 90))

# print str(len(durations))
# print durations