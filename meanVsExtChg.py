from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import LoadDataYear

# precip distribution over region

ext = True
chg = True

models = ['ccsm4', 'gfdl-cm3', 'mri-cgcm3']
modelColors = ['r', 'b', 'g', 'k', 'm']

latRange = [20,35]
lonRange = [75,95]

baseYears = [1980, 2005]
futureYears = [2041, 2060]

latTarget = 30
lonTarget = 85

baseMeanPrecip = []
baseMeanStd = []
baseExtPrecip = []
baseExtStd = []
futureMeanPrecip = []
futureMeanStd = []
futureExtPrecip = []
futureExtStd = []

plt.figure()
plt.hold(True)

for m in range(0, len(models)):
    yearMean = []
    yearExt = []
    for y in range(baseYears[0], baseYears[1]):
        #print 'loaded year ' + str(y)
        d = LoadDataYear.loadDataYear(y, models[m], 'tasmax', reallat = latTarget, reallon = lonTarget)
        yearMean.append(np.mean(d[2])*60*60*24)
        yearExt.append(np.max(d[2])*60*60*24)
    baseMeanStd.append(np.std(yearMean))
    baseExtStd.append(np.std(yearExt))
    baseMeanPrecip.append(np.mean(yearMean))
    baseExtPrecip.append(np.mean(yearExt))

    if chg:
        yearMean = []
        yearExt = []
        for y in range(futureYears[0], futureYears[1]):
            #print 'loaded year ' + str(y)
            d = LoadDataYear.loadDataYear(y, models[m], 'tasmax', reallat = latTarget, reallon = lonTarget)
            yearMean.append(np.mean(d[2])*60*60*24)
            yearExt.append(np.max(d[2])*60*60*24)
        futureMeanStd.append(np.std(yearMean))
        futureExtStd.append(np.std(yearExt))
        futureMeanPrecip.append(np.mean(yearMean))
        futureExtPrecip.append(np.mean(yearExt))
            
meanChg = []
extChg = []
for i in range(0, len(models)):
    meanChg.append(futureMeanPrecip[i]-baseMeanPrecip[i])
    extChg.append(futureExtPrecip[i]-baseExtPrecip[i])


#plt.figure()
#plt.hold(True)

for m in range(0, len(models)):
    #plt.plot(meanChg[m], extChg[m], str('.' + modelColors[m]))
    print models[m]
    print meanChg[m], baseMeanStd[m]
    print extChg[m], baseExtStd[m]
    print


#plt.axis([0, 0.2, 0, 0.2])
#plt.title('Extreme vs. daily precip change')
#plt.savefig('precip-ext-dist-chg.png')
#plt.show()


    



