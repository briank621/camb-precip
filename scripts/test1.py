# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 17:39:01 2016

@author: JackieRyu
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy
import LoadDataYear 
import GetDataMap
import AreaAvgOverTime

#print LoadDataYear.loadDataYear(1985, 'csiro-mk3-6-0', 1, 'tasmax' , latindex = -1, lonindex = -1, reallat = -1, reallon = -1)
#print GetDataMap.getDataMap([20,36], [76,92], 1985, 'csiro-mk3-6-0', 1, 'tasmax')

latRange = [20,36]
lonRange = [76,92]

avgOverTimeBase = AreaAvgOverTime.AreaAvgOverTime('tasmax', ['csiro-mk3-6-0'], 1, [1985,2005], [20,36], [76,92])


tempDataLat = avgOverTimeBase[0]
tempDataLon = avgOverTimeBase[1]
tempDataData = avgOverTimeBase[2]

flatTLat = np.array(tempDataLat)
flatTLon = np.array(tempDataLon)
flatTData = np.array(tempDataData)
print flatTData

m = Basemap(width=10000000/8,height=7000000/8,
            resolution='l',projection='stere',
            lat_ts = 40, lat_0=sum(latRange)/2, lon_0 = sum(lonRange)/2)

lon, lat = np.meshgrid(flatTLon[0,:], flatTLat[:,0])
x, y = m(lon,lat)

cs = m.pcolor(x,y,np.squeeze(flatTData), vmin=-10, vmax=40)

# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='right', pad="10%")

# Add Title
plt.title('Mean Precipitation in 2041-2060 Relative to 1980-2004')
plt.xlabel('Precipitation (mm/day)')

plt.show()