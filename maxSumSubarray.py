'''
Kadane's Algorithm to Maximum Sum Subarray Problem
v=86CQq3pKSUw
'''

def MaxSumSubarray(arr):
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        #print(arr[i])
        max_current = max(arr[i], arr[i]+max_current)
        if max_current > max_global:
            max_global = max_current
    
    return max_global
    
#driver code

A= [-2, 3, 2, -1]
print(MaxSumSubarray(A))
            
