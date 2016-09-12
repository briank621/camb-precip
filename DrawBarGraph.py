from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy

def draw(k, v, title, xlabel, ylabel):
	plt.bar(k, v, 1/1.5, color="blue")
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)