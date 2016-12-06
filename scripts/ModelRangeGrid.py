# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 15:52:59 2016

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
csiro = ['csiro-mk3-6-0']
models = ['noresm1-m', 'cnrm-cm5', 'bnu-esm', 'ccsm4', 'hadgem2-es']
var = 'pr'
ensembleM = [1]
ensembleC = range(1, 11)
monthStart = 1
monthEnd = 12

CAvgOverTime = []
MAvgOverTime = []

for i in range(0, len(csiro)):
    for j in range(0, len(ensembleC)):
    	CAvgOverTime.append(AreaAvgOverTime.AreaAvgOverTime(var, [csiro[i]], [ensembleC[j]], [1985,2005], latRange, lonRange, monthStart, monthEnd))

for i in range(0, len(models)):
    for j in range(0, len(ensembleM)):
    	MAvgOverTime.append(AreaAvgOverTime.AreaAvgOverTime(var, [models[i]], [ensembleM[j]], [1985,2005], latRange, lonRange, monthStart, monthEnd))


# print sumOverTime[2]
lat = CAvgOverTime[0][0]
lon = CAvgOverTime[0][1]

lowValuesC = []
highValuesC = []
lowValuesM = []
highValuesM = []

print "CAVg: " + str(len(CAvgOverTime))
print "CAVg[0]: " + str(len(CAvgOverTime[0]))
print "CAVg[0][0]: " + str(len(CAvgOverTime[0][0]))

for i in range(0,len(CAvgOverTime[0][0])):
    rowC_low = []
    rowC_high = []
    for j in range(0,len(CAvgOverTime[0][0][i])):
        gridboxesC = []
        for z in range(0,len(CAvgOverTime)): 
            gridboxesC.append(CAvgOverTime[z][2][i][j])
        rowC_low.append(np.percentile(gridboxesC,25))
        rowC_high.append(np.percentile(gridboxesC,75))        
    lowValuesC.append(rowC_low)
    highValuesC.append(rowC_high)


for i in range(0,len(MAvgOverTime[0][0])):
    rowM_low = []
    rowM_high = []
    for j in range(0,len(MAvgOverTime[0][0][i])):
        gridboxesM = []
        for z in range(0,len(MAvgOverTime)): 
            gridboxesM.append(MAvgOverTime[z][2][i][j])
        rowM_low.append(np.percentile(gridboxesM,25))
        rowM_high.append(np.percentile(gridboxesM,75))
    lowValuesM.append(rowM_low)
    highValuesM.append(rowM_high)

rangeC = []
rangeM = []

for i in range(len(lowValuesC)):
	diffC = []
	diffM = []
	for j in range(len(lowValuesC[0])):
		diffC.append(highValuesC[i][j] - lowValuesC[i][j])
		diffM.append(highValuesM[i][j] - lowValuesM[i][j])
	rangeC.append(diffC)
	rangeM.append(diffM)

offset = []
for i in range(len(rangeC)):
	row = []
	for j in range(len(rangeC[0])):
		row.append(rangeC[i][j] / rangeM[i][j])
	offset.append(row)

tempDataLat = lat
tempDataLon = lon
tempDataData = offset
print "lat: " + str(len(tempDataLat))
print "lon: " + str(len(tempDataLat))
# print "offset: " + str(len(tempDataData))

flatTLat = np.array(tempDataLat)
flatTLon = np.array(tempDataLon)
flatTData = np.array(tempDataData)
print flatTData
# print "flatlat: " + str(flatTLat)
# print "flatlon: " + str(flatTLon)

minVal = 0
maxVal = 1

plt.figure()
title = 'Difference in Offset for Mean Precipitation Between Models From 1985-2005'
xlabel = 'Quotient of the Range for Precipitation'
DrawBaseMap.drawMap(flatTLon, flatTLat, flatTData, latRange, lonRange,
                     minVal, maxVal, title, xlabel, False)

plt.show()