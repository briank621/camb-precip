from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy
import AreaAvgOverTime
import GetDataMap

ext = True

models = ['ccsm4', 'gfdl-cm3', 'hadgem2-es', 'cnrm-cm5', 'mri-cgcm3']

latRange = [22,37]
lonRange = [75,95]

if ext:
    avgOverTimeBase = AreaAvgOverTime.AreaExtremeAvgOverTime('tasmax', models, [1980,2005], latRange, lonRange)
    avgOverTimeFuture = AreaAvgOverTime.AreaExtremeAvgOverTime('tasmax', models, [2041,2060], latRange, lonRange)
    avgOverTime = AreaAvgOverTime.AreaAvgDifference(avgOverTimeBase, avgOverTimeFuture)
else:
    avgOverTimeBase = AreaAvgOverTime.AreaAvgOverTime('tasmax', models, [1980,2005], latRange, lonRange)
    avgOverTimeFuture = AreaAvgOverTime.AreaAvgOverTime('tasmax', models, [2041,2060], latRange, lonRange)
    avgOverTime = AreaAvgOverTime.AreaAvgDifference(avgOverTimeBase, avgOverTimeFuture)

tempDataLat = avgOverTimeBase[0]
tempDataLon = avgOverTimeBase[1]
tempDataData = avgOverTime

flatTLat = np.array(tempDataLat)
flatTLon = np.array(tempDataLon)
flatTData = np.array(tempDataData)

m = Basemap(width=10000000/7,height=7000000/7,
            resolution='l',projection='stere',
            lat_ts = 40, lat_0=sum(latRange)/2, lon_0 = sum(lonRange)/2)

lon, lat = np.meshgrid(flatTLon[0,:], flatTLat[:,0])
x, y = m(lon,lat)
cs = m.pcolor(x,y,np.squeeze(flatTData), vmin=0, vmax=5)

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
plt.title('Annual maximum temperature change')
plt.xlabel('Temperature (degrees C)')

plt.savefig('tasmax-ext-diff.png')
plt.show()
