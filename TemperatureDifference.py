# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 23:42:58 2015

@author: JackieRyu
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 09:35:54 2015

@author: ethan
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy
import LatLonIndex
import GetDataMap

upLat = 40
lowLat = 20
lftLon = 70
rgtLon = 100

latLonRange = LatLonIndex.findLatLonRange([lowLat, upLat], [lftLon, rgtLon], [])

latRange = latLonRange[0]
lonRange = latLonRange[1]
Data = GetDataMap.getDataMap(latRange,lonRange,2004,"tasmax")
print len(Data[2])
print len(Data[2][0])
Data_average = GetDataMap.getTimeAvg(Data[2])
tempDataLat = Data[0]
tempDataLon = Data[1]
tempDataData = Data_average[2]

flatTLat = np.array(tempDataLat)
flatTLon = np.array(tempDataLon)
flatTData = np.array(tempDataData)

m = Basemap(width=10000000/5,height=7000000/5,
            resolution='l',projection='stere',\
            lat_ts=40,lat_0=(upLat+lowLat)/2,lon_0=(lftLon+rgtLon)/2)

lon, lat = np.meshgrid(flatTLon[0,:], flatTLat[:,0])
x, y = m(lon,lat)
cs = m.pcolor(x,y,np.squeeze(flatTData), vmin=min(min(x) for x in flatTData), vmax=max(max(x) for x in flatTData))

# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")

# Add Title
plt.title('Temperature Difference 2000-2004 Relative to 1990-1995')

plt.show()

