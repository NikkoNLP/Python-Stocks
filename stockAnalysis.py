import numpy as np

# Takes 1-D array of seasonal medians and returns an array 
# of differences between that month and the next MAX_DATA_STEP months.
# organizes data into MAX_COUNTER groups.
MAX_COUNTER= 12
MAX_DATA_STEP = 11

def getDiff(arr):

	seasonCounter = 0
	
	totalArray = []
	
	for x in xrange(0,MAX_COUNTER):
		totalArray.append([])
	
	for index, val in enumerate(arr):

		if index >= len(arr) - MAX_DATA_STEP:
			break
	
		seasonCounter %= MAX_COUNTER
	
		tmpArr = []	
		for i in xrange(1, MAX_DATA_STEP+1):
			tmpArr.append(arr[index+i] - val)
		
		#Append to appropriate season list
		totalArray[seasonCounter].append(tmpArr)
		
		seasonCounter += 1
	
	return totalArray

#takes a 2-d array of differences and returns an array of the mean and s.d. for each difference:
def getMeans(diffArr):
	returnArr = []
	for seasonArr in diffArr:
		returnArr.append(zip(np.mean(seasonArr, axis=0),np.std(seasonArr,axis=0)))
	
	return returnArr
	
	
	
	
	
	