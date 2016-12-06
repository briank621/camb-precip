from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy


def draw(sumOverTime):
	plt.figure()
	data = sumOverTime
	bp = plt.boxplot(data, patch_artist=True)

	## change outline color, fill color and linewidth of the boxes
	for box in bp['boxes']:
	    # change outline color
	    box.set( color='#7570b3', linewidth=1)
	    # change fill color
	    box.set( facecolor = '#1b9e77' )

	## change color and linewidth of the whiskers
	for whisker in bp['whiskers']:
	    whisker.set(color='#7570b3', linewidth=1)

	## change color and linewidth of the caps
	for cap in bp['caps']:
	    cap.set(color='#7570b3', linewidth=1)

	## change color and linewidth of the medians
	for median in bp['medians']:
	    median.set(color='#b2df8a', linewidth=1)

	## change the style of fliers and their fill
	for flier in bp['fliers']:
	    flier.set(marker='o', color='#e7298a', alpha=0.5)