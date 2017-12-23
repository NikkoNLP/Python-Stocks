import numpy as np

# Takes 1-D array of seasonal medians and returns an array 
# of differences between that season and the next 3

# input: [w1, sp1, su1, f1, ... wn, spn, sun, fn]
# output: [[winter diffs],[spring diffs], [summer diffs], [fall diffs]]

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

#takes a 2-d array of differences and returns an array of the mean and s.d. for each difference:
#input: [[winter diffs],[spring diffs], [summer diffs], [fall diffs]]
#output: [[winter (mean,s.d),(mean,s.d)...],[sprint mean/s.d.], [summer mean/s.d.], [fall mean/s.d.]]
def getMeans(diffArr):
	returnArr = []
	for seasonArr in diffArr:
		returnArr.append(zip(np.mean(seasonArr, axis=0),np.std(seasonArr,axis=0)))
	
	return returnArr
	
	
	
	
	
	