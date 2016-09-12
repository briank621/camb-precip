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
models = ['csiro-mk3-6-0']
ncep = ['ncep']
var = 'prate'
# models = ['noresm1-m', 'cnrm-cm5', 'bnu-esm', 'ccsm4', 'hadgem2-es']
# ensemble = [1]
# ensemble = range(1, 11)
monthStart = 1
monthEnd = 12
# monthsStart = [12, 3, 6, 9]
# monthsEnd = [2, 5, 8, 11]

sumOverTimeBase = AreaAvgOverTime.AreaSumOverTime(var, ncep, [-1], [1985,2005], latRange, lonRange, monthStart, monthEnd)

# sumOverTimeComp = AreaAvgOverTime.AreaSumOverTime('pr', models, ensemble, [1985,2005], latRange, lonRange, monthStart, monthEnd)

if var == 'prate':
	for i in range(0,len(sumOverTimeBase[2])):
		sumOverTimeBase[2][i]*=60*60*24
		# sumOverTimeComp[2][i]*=60*60*24

# print str(sumOverTimeBase)

tempDataLat = sumOverTimeBase[0]
tempDataLon = sumOverTimeBase[1]
tempDataData = sumOverTimeBase[2]
tempDataData = AreaAvgOverTime.SumAvgDifference(sumOverTimeBase, sumOverTimeComp)

flatTLat = np.array(tempDataLat)
flatTLon = np.array(tempDataLon)
flatTData = np.array(tempDataData)
print flatTData

y = flatTData
N = len(y)
x = range(N)
width = 1/1.5
plt.bar(x, y, width, color="blue")

# Add Title
# plt.title('Weekly Precipitation in Cambodia From 1985-2005  ')
plt.title('Difference Weekly Precipitation in Cambodia From 2045-2065 To 1985-2005  ')
plt.xlabel('Weeks of the Year')
# plt.ylabel('Precipitation (mm/day)')

plt.show()