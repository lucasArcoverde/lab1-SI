
def maximo(array):
	maxElement = array[0]
	
	for i in array:
		if (i > maxElement):
			maxElement = i
	return maxElement
