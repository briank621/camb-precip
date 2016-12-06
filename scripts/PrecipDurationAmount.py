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
import DrawBarGraph

def makeBarGraph(years, yeare):
	dic = dict()
	for y in range(years, yeare+1):
		print y
		g = GetDataMap.getDataMap(latRange, lonRange, y, m, e, var)
		for i in range(len(g[2])):
			for j in range(len(g[2][i])):
				consec = 0
				amt = 0
				for d in range(dayStart, dayEnd):
					val = g[2][i][j][d]*60*60*24
					if(val > 10):
						consec += 1
						amt += val
					elif consec > 0:
						if(consec in dic):
							dic[consec].append(amt/consec)
						else:
							dic[consec] = [amt/consec];
						consec = 0
						amt = 0

	print str(len(dic))
	avgD = dict()
	for k in dic:
		avgD[k] = sum(dic[k])/len(dic[k])
	plt.figure()
	DrawBarGraph.draw(avgD.keys(), avgD.values(), "Average Amount of Precipitation"+ 
		"For Consecutive Days  " + "(%d, %d)" % (years, yeare), 
		'Number of Consecutive Days (Model: ' + m + ')',
	    'Average Amount of Precipitation (mm/day)')


latRange = [13,15]
lonRange = [106,108]
models = ['noresm1-m', 'cnrm-cm5', 'bnu-esm', 'ccsm4', 'hadgem2-es']
# models = ['noresm1-m']
var = 'pr'
ensemble = [1]
pastYears = range(1985, 2005)
futureYears = range(2045, 2065)
# ensemble = range(1, 11)
dayStart = 60
dayEnd = 328
precip = []
durations = []

for m in models:
	print m
	for e in ensemble:
		print "Ensemble: " + str(e)
		makeBarGraph(1985, 2005)
		makeBarGraph(2045, 2065)

plt.show()



