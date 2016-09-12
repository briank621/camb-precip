import matplotlib.pyplot as plt
import numpy as np
import LoadDataYear

# precip distribution over region

chg = True

models = ['ccsm4', 'gfdl-cm3', 'mri-cgcm3']

latRange = [20,35]
lonRange = [75,95]

baseYears = [1980, 2005]
futureYears = [2041, 2060]

latTarget = 30
lonTarget = 85

dryThresh = [1, 2, 5, 10, 15, 20] # mm/day

baseDryInterval = []
futureDryInterval = []

rainy = False
dayRange=range(0, 360)
if rainy:
    dayRange = range(180, 270)
else:
    dayRange = range(0, 90)

dayRange = range(90, 180)

for thresh in dryThresh:
    base = []
    future = []
    for m in range(0, len(models)):

        for y in range(baseYears[0], baseYears[1]):
            count = 0
            curData = LoadDataYear.loadDataYear(y, models[m], 'pr', reallat = latTarget, reallon = lonTarget)
            for d in curData[2][dayRange[0]:dayRange[-1]]:
                if d*60*60*24 < thresh:
                    count += 1
                else:
                    base.append(count)
                    count = 0

        if chg:
            for y in range(futureYears[0], futureYears[1]):
                count = 0
                curData = LoadDataYear.loadDataYear(y, models[m], 'pr', reallat = latTarget, reallon = lonTarget)
                for d in curData[2][dayRange[0]:dayRange[-1]]:
                    if d*60*60*24 < thresh:
                        count += 1
                    else:
                        future.append(count)
                        count = 0

    baseDryInterval.append(np.mean(base))
    futureDryInterval.append(np.mean(future))

plt.figure()
plt.hold(True)
plt.plot(dryThresh, baseDryInterval, 'b-', label = 'historical')
plt.plot(dryThresh, futureDryInterval, 'r-', label = 'future')
plt.title("Dry Season interval")
plt.xlabel("Dry threshold (mm/day)")
plt.ylabel("Interval (days)")
plt.legend(loc=2)
plt.savefig("dry-interval-spring.png")
plt.show()

print baseDryInterval
print futureDryInterval