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
models = ['csiro-mk3-6-0']
# models = ['noresm1-m', 'cnrm-cm5', 'bnu-esm', 'ccsm4', 'hadgem2-es']
var = 'pr'
# ensemble = [1]
ensemble = range(1, 11)
monthStart = 1
monthEnd = 12

avgOverTime = []
sumOverTime = []

for i in range(0, len(models)):
    for j in range(0, len(ensemble)):
        sumOverTime.append(AreaAvgOverTime.AreaSumOverTime(var, [models[i]], [ensemble[j]], [1985,2005], latRange, lonRange, monthStart, monthEnd))
# print sumOverTime[2]
lat = sumOverTime[0]
lon = sumOverTime[0]

lowValuesP = []
highValuesP = []
lowValuesF = []
highValuesF = []

print "length" + str(len(sumOverTime))
print "length[0]" + str(len(sumOverTime[0]))
print "length[0][2]: " + str(len(sumOverTime[0][2]))

for i in range(0, len(sumOverTime[0][2])):
    timeBoxes=[]
    for j in range(0, len(sumOverTime)):
        timeBoxes.append(sumOverTime[j][2][i])
    lowValuesP.append(np.percentile(timeBoxes, 25))
    highValuesP.append(np.percentile(timeBoxes, 75))

# for i in range(0,len(avgOverTimePast[0][0])):
#     rowP_low = []
#     rowP_high = []
#     rowF_low = []
#     rowF_high = []
#     for j in range(0,len(avgOverTimePast[0][0][i])):
#         gridboxesP = []
#         gridboxesF = []
#         gridboxes=[]
#         for z in range(0,len(avgOverTimePast)): 
#             gridboxes.append(avgOverTime[z][i][j])
#             # gridboxesP.append(avgOverTimePast[z][2][i][j])
#             # gridboxesF.append(avgOverTimeFuture[z][2][i][j])
#         p25 = np.percentile(gridboxes,25)
#         # p25 = np.percentile(gridboxesP,25)
#         # p75 = np.percentile(gridboxesP,75)
#         # f25 = np.percentile(gridboxesF,25)
#         # f75 = np.percentile(gridboxesF,75)
#         rowP_low.append(p25)
#         # rowP_high.append(p75)
#         # rowF_low.append(f25)
#         # rowF_high.append(f75) 
#     lowValuesP.append(rowP_low)
#     # highValuesP.append(rowP_high)
#     # lowValuesF.append(rowF_low)
#     # highValuesF.append(rowF_high)



# print lowValuesP
# print highValuesP
# print lowValuesF
# print highValuesF



#
for i in range(0,len(lowValuesP)):
   lowValuesP[i]*=60*60*24
   highValuesP[i]*=60*60*24


tempDataLat = lat
tempDataLon = lon
tempDataData = lowValuesP
# print "lat: " + str(len(tempDataLat))
# print "lon: " + str(len(tempDataLat))
# print "lvp: " + str(len(tempDataData))

# flatTLat = np.array(tempDataLat)
# flatTLon = np.array(tempDataLon)
flatTData = np.array(tempDataData)
print flatTData
# print "flatlat: " + str(flatTLat)
# print "flatlon: " + str(flatTLon)

minVal = -5
maxVal = 5

plt.figure()
y = flatTData
N = len(y)
x = range(N)
width = 1/1.5
plt.bar(x, y, width, color="blue")
plt.title('Weekly Precipitation in Cambodia (25th Percentile) from 1985-2005')
plt.xlabel('Weeks of the Year')

plt.figure()
y = np.array(highValuesP)
plt.bar(x, y, width, color="blue")
plt.title('Weekly Precipitation in Cambodia (75th Percentile) from 1985-2005')
plt.xlabel('Weeks of the Year')

plt.show()

# plt.figure()
# title = 'Mean Precipitation in 2041-2060 Relative to 1980-2004 '
# xlabel = 'Precipitation (mm/day) for model: ' + m
# DrawBaseMap.drawMap(flatTLon, flatTLat, flatTData, latRange, lonRange,
#                      minVal, maxVal, title, xlabel, False)

# plt.show()