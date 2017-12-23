## Purpose: Creates an array of medians for each 5 day period
import datetime
import pandas as pd
import numpy as np
import cPickle as pickle
from pandas_datareader import data, wb

PATH = './stock-data/'
EXT = '.p'

## Functions
def getMedian(stockData, startYear, startMonth, startDay, dayDuration):
	startDate = (startMonth - 1) * 21
	endDate = startDate + 21
	sd = stockData[startDate:endDate]

	return np.median(sd.Close)

def stockData(stock,startYear,endYear):
	arr = []
	
	for year in xrange(startYear, endYear + 1):
		filename = PATH + stock + '-' + str(year) + EXT
		stockYear = pickle.load( open(filename, 'rb'))
		
		for month in xrange(1, 13):
			arr.append(getMedian(stockYear, year, month, 1, 21))
	
	return arr

