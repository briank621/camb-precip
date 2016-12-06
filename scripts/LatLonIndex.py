# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scipy.io
import sys # (if you want to call something specific) from sys import maxint

temp = []

#convert from the actual lat/lon values to the indices of the array
#targetlat: the latitude you are looking for
def findLatIndex(targetlat,data):
    diff1 = sys.maxint
    diff2 = 0
    closesti = sys.maxint
    closestj = sys.maxint
    
    i = sys.maxint
    j = sys.maxint

    if len(data) == 0:
        data = scipy.io.loadmat('data/ccsm4/tasmax/tasmax_2004_01_01.mat')   
        data = data['tasmax_2004_01_01'][0]
    
    for i in range(0,len(data[0])):
        for j in range(0, len(data[0][i,:])):
            diff2 = abs(targetlat-data[0][i,j])
            if diff2 < diff1:
               # print diff1, diff2
               # print i, j
                diff1 = diff2
                closesti = i
                closestj = j
    return (closesti, closestj)
    
    #convert from the actual lat/lon values to the indices of the array
    #targetlon: the longitude you are looking for
def findLonIndex(targetlon,data):
    diff1 = sys.maxint
    diff2 = 0
    closesti = sys.maxint
    closestj = sys.maxint
    
    i = sys.maxint
    j = sys.maxint
    
    if len(data) == 0:
        data = scipy.io.loadmat('data/ccsm4/tasmax/tasmax_2004_01_01.mat') 
        data = data['tasmax_2004_01_01'][0]

    for i in range(0,len(data[1])):
        for j in range(0, len(data[1][i,:])):
            diff2 = abs(targetlon-data[1][i,j])
            if diff2 < diff1:
                diff1 = diff2
                closesti = i
                closestj = j
    return (closesti, closestj)
    
    #finds the highest temperature for each grid box over time
def findHighestTemp(data):
    high = sys.maxint
    x = []
    
    for i in range(0,len(data[2])):
        currentRow = []
        for j in range(0, len(data[2][i,:])):
            high = sys.maxint
            for s in range(0, len(data[2][i,j,:])):
                if data[2][i,j,s] > high or high == sys.maxint:
                    high = data[2][i,j,s]
            currentRow.append(high)
        x.append(currentRow)
    return x
    
    #return: range of latitude and longitude indices for the frame we are looking at 
def findLatLonRange(latRange, lonRange, data):
    if len(data) == 0:
        data = scipy.io.loadmat('data/ccsm4/tasmax/tasmax_2004_01_01.mat') 
        data = data['tasmax_2004_01_01'][0]
    x= findLatIndex(latRange[0], data)
    y= findLonIndex(lonRange[0], data)
    z= findLatIndex(latRange[1], data)
    w= findLonIndex(lonRange[1], data)
    
    possibleLat = range(x[0],z[0],1)
    possibleLon = range(y[1],w[1],1)
    
    return (possibleLat,possibleLon)
    

#y = findHighestTemp(tasmax["tasmax_2005_01_01"][0])
#print y[65][142]
#print findLatIndex(42,tasmax["tasmax_2005_01_01"][0])
#print findLongIndex(286,tasmax["tasmax_2005_01_01"][0])
#print tasmax["tasmax_2005_01_01"][0][2][10,10]

#temp = tasmax["tasmax_2005_01_01"][0][2][10,10]
#plt.plot(temp,"g")
#plt.ylabel("Temperature")
#plt.xlabel("Days")
#plt.title("Daily Temperature")

#plt.show()

