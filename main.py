import stockAnalysis
import getdata

fileName = "stocks.txt"

if __name__ == '__main__':
	with open(fileName) as f:
		lines = [line.rstrip('\n') for line in f]

		
		for stock in lines:
			rawData = getdata.stockData(stock, 2000, 2017)
			diffData = stockAnalysis.getDiff(rawData)
			resultData = stockAnalysis.getMeans(diffData)
			print stock + ":"
			
			for season in resultData:
				print season
				for val, sd in season:
					if abs(val) > sd :
						print str(val) + ' ' + str(sd)
			
			print '\n'
