
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy
import AreaAvgOverTime
import GetDataMap
import DrawBarGraph

latRange = [5,20]
lonRange = [90,120]
models = ['csiro-mk3-6-0']
#models = ['noresm1-m', 'cnrm-cm5', 'bnu-esm', 'ccsm4', 'hadgem2-es']
var = 'pr'
ensemble = [1]
# ensemble = range(1, 11)
monthStart = 1
monthEnd = 12
# monthsStart = [12, 3, 6, 9]
# monthsEnd = [2, 5, 8, 11]
yearsum=0
yearsum_old=[]
yearsum_new=[]

years = range(2045,2065)

for m in models:
	print m
	for i in range(2045,2065):
		sumOverTimeBase = AreaAvgOverTime.AreaSumOverTime(var, [m], ensemble, [i,i+1], latRange, lonRange, monthStart, monthEnd)

		if var == 'pr':
			for i in range(0,len(sumOverTimeBase[2])):
				sumOverTimeBase[2][i]*=60*60*24

		print sumOverTimeBase[2]

		tmp=0
		for j in range(len(sumOverTimeBase[2])):
			tmp+=sumOverTimeBase[2][j]
		yearsum_old.append(tmp)

print yearsum_old

DrawBarGraph.draw(years,yearsum_old,"Precipitation Amount Yearly","Year","Amount (mm)")
plt.show()