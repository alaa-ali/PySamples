def sumTwo(arr1, arr2, targetVal):
  diff=set()
  for item in arr1:
    diff.add(targetVal - item)
  for item in arr2:
    if(item in diff): return True
  
  return False

a = [-2, 3,4,5,10]
b = [-9,-5, 6] 
print(sumTwo(a, b, targetVal = 14))

#https://www.youtube.com/watch?v=sfuZzBLPcx4
