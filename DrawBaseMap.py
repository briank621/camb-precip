# -*- coding: utf-8 -*-
"""
Created on Fri July 19, 2016

@author: Brian Kim
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy
import AreaAvgOverTime
import GetDataMap

def drawMap(flatTLon, flatTLat, flatTData, latRange, lonRange, minVal, maxVal, title, xlabel, show=True):
	m = Basemap(width=10000000/8,height=7000000/8,
	            resolution='l',projection='stere',
	            lat_ts = 40, lat_0=sum(latRange)/2, lon_0 = sum(lonRange)/2)

	lon, lat = np.meshgrid(flatTLon[0,:], flatTLat[:,0])
	x, y = m(lon,lat)

	cs = m.pcolor(x,y,np.squeeze(flatTData), vmin=minVal, vmax=maxVal)

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
	plt.title(title)
	plt.xlabel(xlabel)

	if show:
		plt.show()