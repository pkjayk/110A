from flask import Flask
import pandas as pd
import scipy.stats
#import seaborn
#import matplotlib.pyplot as plt
#from pylab import savefig

class Correlation:

	def __init__(self):
		self = self
		self.allWines = pd.read_csv('/app/src/winequality-both.csv', sep=',', header=0)

	def correlateWines(self, wineType, wineCharX, wineCharY):

		wineDict = self.allWines.loc[self.allWines['type']==wineType, :]

		correlation = self.getCorrelation(wineDict[wineCharX], wineDict[wineCharY])

		return "For " + wineType + " wine, the correlation between " + wineCharX + " and " + wineCharY + " is: " + correlation[0]

	def getCorrelation(self, x, y):

		getCorr = scipy.stats.pearsonr(x, y)

		return str(getCorr[0]), str(getCorr[1])


