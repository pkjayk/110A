from flask import Flask
import pandas as pd
import scipy.stats
from scipy.stats import linregress
import numpy as np

class Correlation:

	def __init__(self):
		self = self
		self.allWines = pd.read_csv('/app/src/winequality-both.csv', sep=',', header=0)
		self.wineDict = {}
		self.wineCharX = ""
		self.wineCharY = ""

	def correlateWines(self, wineType, wineCharX, wineCharY):

		wineDict = self.getCharacteristicValues(wineType)

		self.wineDict = wineDict
		self.wineCharX = wineCharX
		self.wineCharY = wineCharY

		correlation = self.getCorrelation(wineDict[wineCharX], wineDict[wineCharY])

		return "For <i>" + wineType + "</i> wine, the correlation between <i>" + wineCharX + "</i> and <i>" + wineCharY + "</i> is: <br><span style='font-weight:800;font-size:16pt;'>" + correlation[0] + "</span>"

	def getCorrelation(self, x, y):

		getCorr = scipy.stats.pearsonr(x, y)

		return str(getCorr[0]), str(getCorr[1])

	def getCharacteristicValues(self, wineType):

		return self.allWines.loc[self.allWines['type']==wineType, :]

	def generateRegressionLine(self):

		slope, intercept, r_value, p_value, std_err = linregress(self.wineDict[self.wineCharX], self.wineDict[self.wineCharY])
		return slope*self.wineDict[self.wineCharX]+intercept