## Purpose: Creates an array of medians for each 5 day period
import datetime
import pandas as pd
import numpy as np
import pickle
from pandas_datareader import data, wb

PATH = './stock-data/'
EXT = '.p'

## Functions
def getMedian(stockData, startYear, startMonth, startDay, dayDuration):
	startDate = datetime.datetime(startYear,startMonth,startDay) - datetime.datetime(startYear, 1, 1)
	endDate = startDate + datetime.timedelta(days=dayDuration)
	sd = stockData[startDate.days:endDate.days]
	return np.median(sd.Close)

def stockData(stock,startYear,endYear):
	arr = []
	
	for year in xrange(startYear, endYear + 1):
		filename = PATH + stock + '-' + str(year) + EXT
		stockYear = pickle.load( open(filename, 'rb'))
		
		for month in xrange(1, 13):
			arr.append(getMedian(stockYear, year, month, 1, 30))
	
	return arr

