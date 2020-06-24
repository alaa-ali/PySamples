import numpy as np
def sortedSquaredArray(arr):
  results = [0] * len(arr) #np.zeros(len(arr))
  left = 0
  right = len(arr)-1
  for i in range(len(arr)-1,-1,-1):
    if(abs(arr[left])>abs(arr[right])):
      results[i] = arr[left]*arr[left]
      left +=1;
    else:
      results[i] = arr[right]*arr[right]
      right -=1;
  return results

a= [-6, -4, 1, 2, 3, 5]
res = sortedSquaredArray(a)
print(res)

'''a = [-6, -4, 1, 2, 4, 5]
buckets = [0] * len(a)
print(buckets)'''
