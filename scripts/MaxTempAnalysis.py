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
models = ['csiro-mk3-6-0']
ensemble = range(1, 11)


# models = ['noresm1-m', 'cnrm-cm5', 'bnu-esm', 'ccsm4']
# models = ['mri-cgcm3']
# ensemble = [1]
var = 'tasmax'
monthStart = 1
monthEnd = 12
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
path = "data/plots/high_res/maxtempavg.eps"
DrawBaseMap.drawMap(flatTLon, flatTLat, flatTData, latRange, lonRange,
					 minVal, maxVal, title, xlabel, path)
