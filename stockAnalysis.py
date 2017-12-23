import numpy as np


def getDiff(arr):
	winterArr = []
	springArr = []
	summerArr = []
	fallArr = []
	seasonCounter = 0
	for index, val in enumerate(arr):

		if index >= len(arr) - 3:
			break
	
		seasonCounter %= 4
	
		tmpArr = []
		tmpArr.append(arr[index+1] - val)
		tmpArr.append(arr[index+2] - val)
		tmpArr.append(arr[index+3] - val)
		
		#Append to appropriate season list
		if seasonCounter == 0:
			winterArr.append(tmpArr)
		elif seasonCounter == 1:
			springArr.append(tmpArr)
		elif seasonCounter == 2:
			summerArr.append(tmpArr)
		else:
			fallArr.append(tmpArr)
			
		seasonCounter += 1
	
	return [winterArr,springArr,summerArr,fallArr]

def getMeans(diffArr):
	#3-D array
	#Year
	#Season
	#difference between season and season + x
	returnArr = []
	for seasonArr in diffArr:
		returnArr.append(zip(np.mean(seasonArr, axis=0),np.std(seasonArr,axis=0)))
	
	return returnArr
	
	
	
	
	
	