# Python3 program to find sub-array 
# having maximum sum of elements modulo m. 

# Return the maximum sum subarray mod m. 
def maxSubarray(arr, m): 

	x = 0
	prefix = 0
	maxim = 0

	S = set()
	S.add(0)

	# Traversing the array. 
	for idx in range(len(arr)):
		# Finding prefix sum. 
		prefix = (prefix + arr[idx]) % m
		#print(idx)
		# Finding maximum of prefix sum. 
		maxim = max(maxim, prefix) 

		# Finding iterator poing to the first 
		# element that is not less than value 
		# "prefix + 1", i.e., greater than or 
		# equal to this value. 
		it = 0
		for item in S:
		    #print(item)
		    if item > prefix:
		        print(item)
		        it = item
		        break
		if (it != 0) : 
				maxim = max(maxim, prefix - it + m ) 

		# adding prefix in the set. 
		S.add(prefix) 

	return maxim 

# Driver Code 
arr = [3, 3, 9, 9, 5] 
m = 7
print(maxSubarray(arr, m)) 

# This code is contributed by 
# Shubham Singh(SHUBHAMSINGH10) 
