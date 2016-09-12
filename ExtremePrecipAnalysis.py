# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 19:18:55 2015

@author: JackieRyu
"""

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

latRange = [20,35]
lonRange = [75,95]

avgOverTimeBase = AreaAvgOverTime.AreaExtremeAvgOverTime('pr', 'ccsm4', [1980,1999], latRange, lonRange)
avgOverTimeFuture = AreaAvgOverTime.AreaExtremeAvgOverTime('pr','ccsm4', [2041,2060], latRange, lonRange)

avgOverTimeBase = AreaAvgOverTime.AreaExtremeAvgOverTime('pr', ['gfdl-cm3', 'ccsm4', 'mri-cgcm3', 'hadgem2-es'], [1980,2005], latRange, lonRange)
avgOverTimeFuture = AreaAvgOverTime.AreaExtremeAvgOverTime('pr', ['gfdl-cm3', 'ccsm4', 'mri-cgcm3', 'hadgem2-es'], [2041,2060], latRange, lonRange)

avgOverTime = AreaAvgOverTime.AreaAvgDifference(avgOverTimeBase, avgOverTimeFuture)

tempDataLat = avgOverTimeBase[0]
tempDataLon = avgOverTimeBase[1]
tempDataData = avgOverTime

flatTLat = np.array(tempDataLat)
flatTLon = np.array(tempDataLon)
flatTData = np.array(tempDataData)

m = Basemap(width=10000000/5,height=7000000/5,
            resolution='l',projection='stere',
            lat_ts = 40, lat_0=sum(latRange)/2, lon_0 = sum(lonRange)/2)

lon, lat = np.meshgrid(flatTLon[0,:], flatTLat[:,0])
x, y = m(lon,lat)
cs = m.pcolor(x,y,np.squeeze(flatTData), vmin=-5e-4, vmax=5e-4)

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
plt.title('Annual maximum precipitation in 2041-2060 relative to 1980-2004')
plt.xlabel('Precipitation (mm/day)')

plt.savefig('precip-ext-diff.png')
plt.show()