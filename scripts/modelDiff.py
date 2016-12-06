import matplotlib.pyplot as plt
import numpy as np
import LoadDataYear

# precip distribution over region

ext = False
chg = True

models = ['ccsm4', 'gfdl-cm3','mri-cgcm3']
modelColors = ['r', 'b', 'g', 'k', 'm']

latRange = [20,35]
lonRange = [75,95]

baseYears = [1980, 2005]
futureYears = [2041, 2060]

latTarget = 30
lonTarget = 85

baseModelData = {}
futureModelData = {}
histograms = {}

numBins = 50

plt.figure()
plt.hold(True)

for m in range(0, len(models)):
    baseModelData[models[m]] = []
    for y in range(baseYears[0], baseYears[1]):
        print 'loaded year ' + str(y)
        d = LoadDataYear.loadDataYear(y, models[m], 'pr', reallat = latTarget, reallon = lonTarget)
        if ext:
            baseModelData[models[m]].append(max(d[2])*60*60*24)
        else:
            for x in d[2]:
                baseModelData[models[m]].append(x*60*60*24)

    if chg:
        futureModelData[models[m]] = []
        for y in range(futureYears[0], futureYears[1]):
            print 'loaded year ' + str(y)
            d = LoadDataYear.loadDataYear(y, models[m], 'pr', reallat = latTarget, reallon = lonTarget)
            if ext:
                futureModelData[models[m]].append(max(d[2])*60*60*24)
            else:
                for x in d[2]:
                    futureModelData[models[m]].append(x*60*60*24)

        histograms[models[m]] = np.histogram([a2 - a1 for a2, a1 in zip(futureModelData[models[m]], baseModelData[models[m]])], bins=numBins)
    else:
        histograms[models[m]] = np.histogram(baseModelData[models[m]], bins=numBins)    

    x = list(histograms[models[m]][1][0:numBins])
    y = list(histograms[models[m]][0][0:numBins])

    if not chg:
        total = sum(y);
        for i in range(len(y)):
            y[i] = y[i]/float(total)
    
    plt.plot(x, y, modelColors[m], label = models[m])

plt.xlabel('mm/day')

print y

if chg:
    plt.ylabel('occurances')
    if ext:
        plt.axis([-0.2, 0.5, 0, 10])
    else:
        plt.axis([-10, 10, 0, 4500])
else:
    plt.axis([-0.2, 0.2, -0.01, 0.7])
    plt.ylabel('probability')
plt.title('Precipitation distribution change')
plt.legend()
plt.savefig('precip-dist-chg.png')
plt.show()


    



