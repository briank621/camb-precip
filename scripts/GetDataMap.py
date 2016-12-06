# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:50:44 2015

@author: claireyun
"""

import LoadDataYear
import LatLonIndex
import scipy.io

#latRange: a list containing to integer values for the start and the end
#lonRange: a list containing to integer values for the start and the end
#year: integer
#model: the string name of the model
#var: the string variable from the climate model
#return: list of latitude in the grid box(2D), list of longitude in the grid box(2D), list of data points at the lat,lon and the time-data at that day(3D)
def getDataMap(latRange, lonRange, year, model, ensemble, var):
    # load test data file
    if ensemble == -1:
        testdata = scipy.io.loadmat(str('data/' + model + '/' + var +'/' + var + '_' + str(year) + '_01' + '_01'))
    else:
        testdata = scipy.io.loadmat(str('data/' + model + '/' + 'r' + str(ensemble) +'i1p1'+ '/' + var +'/' + var + '_' + str(year) + '_01' + '_01'))
    testdata = testdata[str(var + '_' + str(year) + '_01' + '_01')][0]
    latLonRange = LatLonIndex.findLatLonRange(latRange, lonRange, testdata)
    
    dataMap = []
    lat=[]
    lon=[]
    for i in latLonRange[0]:
        row = []
        latrow=[]
        lonrow=[]
        for j in latLonRange[1]:
            x = LoadDataYear.loadDataYear(year, model, ensemble, var, latindex = i, lonindex = j)
            latrow.append(x[0])
            lonrow.append(x[1])
            row.append(x[2])
        dataMap.append(row)
        lat.append(latrow)
        lon.append(lonrow)
    return [lat,lon,dataMap]
    
#return 1d array- avg temp for each day averaged over x, y coordinates
def getAreaAvg(data):    
    dailySum = []
    for i in range(len(data[0][0])):
        dailySum.append(0)
        for j in range(len(data)):
            for r in range(len(data[0])):
                dailySum[i] += data[j][r][i]
        dailySum[i] /= (len(data)*len(data[0]))
    return dailySum
    
#data:a three-dimensional array containing lat lon data
#return: 2d grid of the avg values over a time at each grid box 
def getTimeAvg(data):
    timeSum = []
    for i in range(len(data)):
        row = []
        for j in range(len(data[0])):
            row.append(sum(data[i][j])/len(data[i][j]))
        timeSum.append(row)
    return timeSum

#data:a three-dimensional array containing lat lon data
#return: 2d grid of the avg values over a time at each grid box 
def leapYear(n):
    return (n % 400 == 0) or ((n%4 == 0) and (n % 100 != 0));

def initializeStartStop(start, end, year):
    start-=1
    end-=1
    dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    datesL = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(leapYear(year)):
        d = dates
        stop = 365 #the hadgem model only has 328 days
    else:
        d = dates
        stop = 365

    startIndex = 0
    for i in range(1, start):
        startIndex += d[i-1]

    if(start > end):
        endIndex = 0
        for i in range(0, end):
            endIndex += d[i]
    else:
        endIndex = startIndex
        # print "start:%d, end: %d, stop: %d" % (startIndex, endIndex, stop)
        for i in range(start, end+1):
            endIndex += d[i]

    if endIndex > 328:
        endIndex = 365

    return (startIndex, endIndex, stop)

def getWeeklySum(data, year, start, end, nextData=None):
    (startIndex, endIndex, stop) = initializeStartStop(start, end, year)
    # print "numDays: %d" % (len(data[0][0]))
    # print "%d:%d:%d" % (startIndex, endIndex, stop)
    weeklySum = []
    if(start > end):
        for k in range(startIndex, stop, 7):
            for l in range(0, 7):
                total = 0
                for i in range(len(data)):
                    for j in range(len(data[0])):
                        if(k+l < stop):
                            total += data[i][j][k+l]
                        else:
                            total += nextData[i][j][(k+l)%stop]
            weeklySum.append(total)
        for k in range(7 - ((stop - startIndex)%7), endIndex, 7):
            for l in range(0, 7):
                total = 0
                for i in range(len(data)):
                    for j in range(len(data[0])):
                        total += nextData[i][j][(k+l)%stop]
            weeklySum.append(total)
    else:
        for k in range(startIndex, stop, 7):
            for l in range(0, 7):
                total = 0
                for i in range(len(data)):
                    for j in range(len(data[0])):
                        #print "days: %d" % (k+l)
                        total += data[i][j][(k+l)%stop]
            weeklySum.append(total)
    return weeklySum

def getMonthAvg(data, year, start, end, nextData=None):
    (startIndex, endIndex, stop) = initializeStartStop(start, end, year)
    # print "start: %d \t end: %d" % (startIndex, endIndex)
    # print "data: " + str(len(data))
    # print "data[0]: " + str(len(data[0]))
    # print "data[0][0]: " + str(len(data[0][0]))

    timeSum = []
    if(start > end):
        for i in range(len(data)):
            row=[]
            for j in range(len(data[0])):
                total = 0
                for k in range(startIndex, stop):
                    total += data[i][j][k]
                for k in range(0, endIndex):
                    total += nextData[i][j][k]
                row.append(total/(stop - startIndex))
            timeSum.append(row)
    else:
        # print "(%d, %d)" % (len(data), len(data[0]))
        # print "(%d, %d)" % (startIndex, endIndex)
        for i in range(len(data)):
            row=[]
            for j in range(len(data[0])):
                total = 0

                for k in range(startIndex, endIndex):
                    total += data[i][j][k]
                row.append(total/(endIndex - startIndex))
            timeSum.append(row)
    return timeSum