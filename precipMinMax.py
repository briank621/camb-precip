
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy
import AreaAvgOverTime
import GetDataMap
import DrawBarGraph

latRange = [5,20]
lonRange = [90,120]
#models = ['csiro-mk3-6-0']
models = ['noresm1-m', 'cnrm-cm5', 'bnu-esm', 'ccsm4', 'hadgem2-es']
var = 'pr'
ensemble = [1]
#ensemble = range(1, 11)
monthStart = 1
monthEnd = 12
# monthsStart = [12, 3, 6, 9]
# monthsEnd = [2, 5, 8, 11]
yearsum=0
yearsum_old=[]
yearsum_new=[]

years = range(1985,2005)

for m in models:
	print m
	yearsum_old=[]
	for i in range(1985,2005):
		sumOverTimeBase = AreaAvgOverTime.AreaSumOverTime(var, [m], ensemble, [i,i+1], latRange, lonRange, monthStart, monthEnd)

		if var == 'pr':
			for i in range(0,len(sumOverTimeBase[2])):
				sumOverTimeBase[2][i]*=60*60*24

		tmp=0
		for j in range(len(sumOverTimeBase[2])):
			tmp+=sumOverTimeBase[2][j]
		yearsum_old.append(tmp)

yearsum_min=99999
for i in yearsum_old:
	if i < yearsum_min:
		yearsum_min = i

yearsum_max=0
for i in yearsum_old:
	if i > yearsum_max:
		yearsum_max = i

print "99p: " + str(np.percentile(yearsum_old, 99))
print "90p: " + str(np.percentile(yearsum_old, 90))
print "50p: " + str(np.percentile(yearsum_old, 50))
print "25p: " + str(np.percentile(yearsum_old, 25))
print "10p: " + str(np.percentile(yearsum_old, 10))
print "5p: " + str(np.percentile(yearsum_old, 5))
print "1p: " + str(np.percentile(yearsum_old, 1))

print yearsum_min
print yearsum_max

years = range(2045,2065)

for m in models:
	print m
	yearsum_new=[]
	for i in range(2045,2065):
		sumOverTimeBase = AreaAvgOverTime.AreaSumOverTime(var, [m], ensemble, [i,i+1], latRange, lonRange, monthStart, monthEnd)

		if var == 'pr':
			for i in range(0,len(sumOverTimeBase[2])):
				sumOverTimeBase[2][i]*=60*60*24

		tmp=0
		for j in range(len(sumOverTimeBase[2])):
			tmp+=sumOverTimeBase[2][j]
		yearsum_new.append(tmp)

yearsum_min=99999
for i in yearsum_new:
	if i < yearsum_min:
		yearsum_min = i

yearsum_max=0
for i in yearsum_new:
	if i > yearsum_max:
		yearsum_max = i

print "99p: " + str(np.percentile(yearsum_new, 99))
print "90p: " + str(np.percentile(yearsum_new, 90))
print "50p: " + str(np.percentile(yearsum_new, 50))
print "25p: " + str(np.percentile(yearsum_new, 25))
print "10p: " + str(np.percentile(yearsum_new, 10))
print "5p: " + str(np.percentile(yearsum_new, 5))
print "1p: " + str(np.percentile(yearsum_new, 1))

print yearsum_min
print yearsum_max
