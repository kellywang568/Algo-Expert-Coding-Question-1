def isValidSubsequence(array, sequence):
	i = j =  0
	while i< len(array) and j<len(sequence):
		if array[i] == sequence[j]:
			j+=1
			i+=1
		else:
			i+=1
	return j == len(sequence)

