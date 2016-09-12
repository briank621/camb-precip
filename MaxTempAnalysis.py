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
models = ['noresm1-m', 'cnrm-cm5', 'bnu-esm', 'ccsm4', 'hadgem2-es']
# models = ['mri-cgcm3']
var = 'tasmax'
monthStart = 1
monthEnd = 12
ensemble = [1]
#seasons from dec to february, march to may, june to august, sep to nov
avgOverTimeBase = AreaAvgOverTime.AreaAvgOverTime(var, models, ensemble, [1985,2005], latRange, lonRange, monthStart, monthEnd)
avgOverTimeFuture = AreaAvgOverTime.AreaAvgOverTime(var,models, ensemble, [2045,2065], latRange, lonRange, monthStart, monthEnd)

avgOverTime = AreaAvgOverTime.AreaAvgDifference(avgOverTimeBase, avgOverTimeFuture)
tempDataLat = avgOverTimeBase[0]
tempDataLon = avgOverTimeBase[1]
tempDataData = avgOverTime

flatTLat = np.array(tempDataLat)
flatTLon = np.array(tempDataLon)
flatTData = np.array(tempDataData)
print flatTData

minVal = -5
maxVal = 5
title = 'Mean Max Temperature in 2045-2065 Relative to 1985-2005 '
xlabel = 'Temperature (C)'
DrawBaseMap.drawMap(flatTLon, flatTLat, flatTData, latRange, lonRange,
					 minVal, maxVal, title, xlabel)
