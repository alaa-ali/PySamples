def maxSubarraySum_Kadane(vec):
    maxSum = vec[0]
    currSum = vec[0]
    for i in range(1, len(vec)):
        currSum = max(vec[i]+currSum, vec[i])
        maxSum = max(currSum, maxSum)
    return maxSum

a = [-2, 2, 5, -11, 6]
maxout = maxSubarraySum_Kadane(a)
print(maxout)
b = [-2, 2, 5, -11, 6, 2]
maxout = maxSubarraySum_Kadane(b)
print(maxout)

print(maxSubarraySum_Kadane([-4, 15, -5, 4, 1]))

#https://www.youtube.com/watch?v=jnoVtCKECmQ
