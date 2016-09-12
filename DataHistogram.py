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
models = ['noresm1-m', 'cnrm-cm5', 'bnu-esm', 'ccsm4', 'hadgem2-es']
# models = ['noresm1-m']
var = 'pr'
ensemble = [1]
years = range(1985, 2005)
# ensemble = range(1, 11)
# monthsStart = [12, 3, 6, 9]
dayStart = 60
dayEnd = 328
precip = []
durations = []

for m in models:
	print m
	for e in ensemble:
		print "Ensemble: " + str(e)
		for y in years:
			# print y
			g = GetDataMap.getDataMap(latRange, lonRange, y, m , e, var)
			for d in range(dayStart, dayEnd):
				for i in range(len(g[2])):
					for j in range(len(g[2][i])):
						val = g[2][i][j][d]*60*60*24
						precip.append(val)

		print "99p: " + str(np.percentile(precip, 99))
		print "90p: " + str(np.percentile(precip, 90))
		print "50p: " + str(np.percentile(precip, 50))
		print "25p: " + str(np.percentile(precip, 25))
		print "10p: " + str(np.percentile(precip, 10))
		print "5p: " + str(np.percentile(precip, 5))
		print "1p: " + str(np.percentile(precip, 1))
# print str(len(precip))
# plt.figure()
# plt.hist(precip)
# plt.title("Histogram of Precipitation values")
# plt.show()



