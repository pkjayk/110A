from flask import Flask
import pandas as pd
import scipy.stats
from scipy.stats import linregress
import numpy as np
from correlation import Correlation
from user import User

class Frequency(Correlation):

	def __init__(self):
		super().__init__()

	def getFrequency(self, wineType, wineCharValue, charA, charB):

		if User.isEmpty(wineCharValue):
			message = 'Wine Characteristic Value cannot be empty.'
			return message, '', ''
		else:
			try:
				wineCharValue = float(wineCharValue)
			except Exception:
				return 'Wine Characteristic Value must be a number.', '', ''

		wineTypeRows = self.getCharacteristicValues(wineType)

		specificRows = wineTypeRows.loc[wineTypeRows[charA] == wineCharValue, :]

		wineCharValueDataset = specificRows.loc[:, charB]

		message = 'I found <i>' + str(wineCharValueDataset.size) + '</i> ' + wineType + ' wines with a <i>' + charA + '</i> of <i>' + str(wineCharValue) + '</i>. Below are the plotted frequencies by wine quality.'

		if wineCharValueDataset.size < 1:
			message = 'No ' + wineType + ' wines were found with a ' + charA + ' of ' + str(wineCharValue) + ''

		return message, wineCharValueDataset, charA

	def getWineType(self, wineType):

		return self.allWines.loc[self.allWines['type']==wineType, :]


