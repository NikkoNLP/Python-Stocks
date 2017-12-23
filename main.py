import stockAnalysis
import getdata

fileName = "stocks.txt"

if __name__ == '__main__':
	with open(fileName) as f:
		lines = [line.rstrip('\n') for line in f]

		
		for stock in lines:
			rawData = getdata.stockData(stock, 2010, 2012)
			diffData = stockAnalysis.getDiff(rawData)
			resultData = stockAnalysis.getMeans(diffData)
			print stock + ":"
			print resultData
			print '\n'