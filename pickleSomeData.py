import cPickle as pickle
import datetime
from pandas_datareader import data, wb

## pickleMe takes the stock and year as input and save a pickled file :)
def pickleMe(stock,year):
	fileName = stock + "-" + str(year)
	startDate = datetime.datetime(year,1,1)
	endDate = startDate + datetime.timedelta(days=365)
	stockData = data.DataReader(stock, "yahoo", startDate, endDate)
	pickle.dump( stockData, open( "./stock-data/" + fileName + ".p", "wb" ) )

## To retreive pickle data
#  a = pickle.load( open( stock-year, "rb" ) )
