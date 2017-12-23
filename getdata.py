## Purpose: Creates an array of medians for each 5 day period
import datetime
import pandas as pd
import numpy as np
from pandas_datareader import data, wb


## Functions
def getMedian(stock, startYear, startMonth, startDay):
	startDate = datetime.datetime(startYear,startMonth,startDay)
	endDate = startDate + datetime.timedelta(days=91)
	sd = data.DataReader(stock, "yahoo", startDate, endDate)
	return np.median(sd.Close)

def stockData(stock,startYear,endYear):
	arr = []
	for y in xrange(startYear, endYear):
		arr.append(getMedian(stock,y -1,12,1))
		arr.append(getMedian(stock,y,3,1))
		arr.append(getMedian(stock,y,6,1))
		arr.append(getMedian(stock,y,9,1))
	return arr

