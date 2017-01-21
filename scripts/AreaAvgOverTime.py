# -*- coding: utf-8 -*-
import GetDataMap
import FindExtremes

#var: the variable given by the model definig what it is looking at ex) 'pr'
#models: the list of models to look at
#timeRange: a range of the time defining the start and the finish
#latRange: the range of the latitude defining the start and the finish
#lonRange: the range of the longitude defininf the start and the finish
#return a two-dimensional list of the latitude and longitue respectively and the avgOverTime(2D): average over multiple models and multiple years  
def AreaAvgOverTime(var, models, ensemble, timeRange, latRange, lonRange, monthStart=1, monthEnd=11):
    avgOverTime = []
    lat = []
    lon = []
    
    for m in range(0, len(models)):
        print "model: " + models[m]
        curEnsAvg = []
        for e in ensemble:
            curModelAvg = []
            print "ensemble: " + str(e)
            for i in range(timeRange[0],timeRange[1]):
                print i
                g = GetDataMap.getDataMap(latRange, lonRange, i, models[m], e, var)
                if len(lat) == 0:
                    lat = g[0]
                    lon = g[1]
        
                # TimeAverage = GetDataMap.getTimeAvg(g[2])
                if(monthStart < monthEnd):
                    TimeAverage = GetDataMap.getMonthAvg(g[2], i, monthStart, monthEnd)
                else:
                    #the month range spans two years
                    # if(i != timeRange[1] - 1):
                    gNext = GetDataMap.getDataMap(latRange, lonRange, i+1, models[m], e, var)
                    # else:
                        # continue
                    TimeAverage = GetDataMap.getMonthAvg(g[2], i, monthStart, monthEnd, gNext[2])
                if(len(curModelAvg) == 0):
                    for j in range(0,len(TimeAverage)):
                        row = []
                        for c in range(0,len(TimeAverage[0])):
                            row.append(TimeAverage[j][c])
                        curModelAvg.append(row)
                else:
                    for j in range(0,len(TimeAverage)):
                        for c in range(0,len(TimeAverage[0])):
                            curModelAvg[j][c] += TimeAverage[j][c]
        
            for i in range(0, len(curModelAvg)):
                for j in range(0, len(curModelAvg[i])):
                    curModelAvg[i][j] /= len(range(timeRange[0],timeRange[1]))

            if len(curEnsAvg) == 0:
                for i in range(0, len(curModelAvg)):
                    row = []
                    for j in range(0, len(curModelAvg[i])):
                        row.append(curModelAvg[i][j])
                    curEnsAvg.append(row)
            else:
                for i in range(0, len(curModelAvg)):
                    for j in range(0, len(curModelAvg[i])):
                        curEnsAvg[i][j] += curModelAvg[i][j]

        for i in range(0, len(curEnsAvg)):
            for j in range(0 ,len(curEnsAvg[i])):
                curEnsAvg[i][j] /= len(ensemble)
        
        if len(avgOverTime) == 0:
            for i in range(0, len(curEnsAvg)):
                row = []
                for j in range(0, len(curEnsAvg[i])):
                    row.append(curEnsAvg[i][j])
                avgOverTime.append(row)
        else:
            for i in range(0, len(curEnsAvg)):
                for j in range(0, len(curEnsAvg[i])):
                    avgOverTime[i][j] += curEnsAvg[i][j]
    
    
    for i in range(0, len(avgOverTime)):
        for j in range(0, len(avgOverTime[i])):        
            avgOverTime[i][j] /= len(models)

    return [lat, lon, avgOverTime]
    
def AreaSumOverTime(var, models, ensemble, timeRange, latRange, lonRange, monthStart=1, monthEnd=12):
    avgOverTime = []
    lat = []
    lon = []
    
    for m in range(0, len(models)):
        print models[m]
        curEnsAvg = []
        for e in ensemble:
            curModelAvg = []
            for i in range(timeRange[0],timeRange[1]):
                print i
                g = GetDataMap.getDataMap(latRange, lonRange, i, models[m], e, var)
                if len(lat) == 0:
                    lat = g[0]
                    lon = g[1]

                if(monthStart < monthEnd):
                    weekSum = GetDataMap.getWeeklySum(g[2], i, monthStart, monthEnd)
                else:
                    #the month range spans two years
                    # if(i != timeRange[1] - 1):
                    gNext = GetDataMap.getDataMap(latRange, lonRange, i+1, models[m], e, var)
                    # else:
                        # continue
                    weekSum = GetDataMap.getWeeklySum(g[2], i, monthStart, monthEnd, gNext[2])


                if(len(curModelAvg) == 0):
                    for j in range(len(weekSum)):
                        curModelAvg.append(weekSum[j]/len(weekSum))
                else:
                    for j in range(len(weekSum)):
                        curModelAvg[j] += weekSum[j]/len(weekSum)
        
            for i in range(0, len(curModelAvg)):
                curModelAvg[i] /= len(range(timeRange[0],timeRange[1]))

            if(len(curEnsAvg) == 0):
                for i in range(len(curModelAvg)):
                    curEnsAvg.append(curModelAvg[i])
            else:
                for i in range(len(curModelAvg)):
                    curEnsAvg[i] += curModelAvg[i]

        for i in range(0, len(curEnsAvg)):
            curEnsAvg[i] /= len(ensemble)
        
        if len(avgOverTime) == 0:
            for i in range(0, len(curEnsAvg)):
                avgOverTime.append(curEnsAvg[i])
        else:
            for i in range(0, len(curEnsAvg)):
                avgOverTime[i] += curEnsAvg[i]
    
    
    for i in range(0, len(avgOverTime)):       
        avgOverTime[i] /= len(models)

    return [lat, lon, avgOverTime]


    #only considers the single highest "var" of each year within the timerange 
    #returns a three dimensional array with lat lon and data 
def AreaExtremeAvgOverTime(var, models, timeRange, latRange, lonRange):
    extAvgOverTime = []
    lat = []
    lon = []
    
    for m in range(0, len(models)):
        curModelExt = []
        for i in range(timeRange[0], timeRange[1]):
            print i
            g = GetDataMap.getDataMap(latRange, lonRange, i, models[m], var)
            if len(lat) == 0:
                lat = g[0]
                lon = g[1]
    
            annualExt = FindExtremes.findAnnualMax(g[2])
            if(len(curModelExt) == 0):
                for j in range(0,len(annualExt)):
                    row = []
                    for c in range(0,len(annualExt[0])):
                        row.append(annualExt[j][c])
                    curModelExt.append(row)
            else:
                for j in range(0,len(annualExt)):
                    for c in range(0,len(annualExt[0])):
                        curModelExt[j][c] += annualExt[j][c]
        
        for i in range(0, len(curModelExt)):
            for j in range(0, len(curModelExt[i])):
                curModelExt[i][j] /= len(range(timeRange[0], timeRange[1]))
                
        if len(extAvgOverTime) == 0:
            for i in range(0, len(curModelExt)):
                row = []
                for j in range(0, len(curModelExt[i])):
                    row.append(curModelExt[i][j])
                extAvgOverTime.append(row)
        else:
            for i in range(0, len(curModelExt)):
                for j in range(0, len(curModelExt[i])):
                    extAvgOverTime[i][j] += curModelExt[i][j]
    
    for i in range(0, len(extAvgOverTime)):
        for j in range(0, len(extAvgOverTime[i])):        
            extAvgOverTime[i][j] /= len(models)
    
    return [lat, lon, extAvgOverTime]
    

def SumAvgDifference(sumTime1, sumTime2):
    sumOverTime = []
    for i in range(0, len(sumTime1[2])):
        sumOverTime.append(sumTime2[2][i] - sumTime1[2][i])
    return sumOverTime

    #subtract the difference between any to two grids (past and future)
    #return a twodimensional array with the substracted value at each position 
def AreaAvgDifference(areaTime1, areaTime2):
    avgOverTime = []
    # print "at1: %d, %d" % (len(areaTime1[2]), len(areaTime1[2][0]))
    # print "at2: %d, %d" % (len(areaTime2[2]), len(areaTime2[2][0]))

    for i in range(0,len(areaTime1[2])):
        row = []
        for j in range(0,len(areaTime1[2][0])):
            row.append(areaTime2[2][i][j]- areaTime1[2][i][j])
        avgOverTime.append(row)
    return avgOverTime