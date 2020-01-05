'''
    Zero Sum Subarray
    v=hLcYp67wCcM
'''
def zeroSum(arr):
    sumDict={}
    total=0
    #for i in range(0, len(arr)+1):
    for i in range(0, len(arr)):
        oldIndex = sumDict.get(total)
        print(sumDict.items())
        print (total)
        
        #if(oldIndex==None and i==len(arr)):
        #    return None
        #elif(oldIndex==None):
        if(oldIndex==None):
            #sumDict.update({oldIndex, i})
            sumDict[total] = i
            total = total + arr[i]
        else:
            result = arr[oldIndex:i]
            return result
            
    return None        

#driver code:
output = zeroSum([6,2,-5,1,2,-1])
print(output)
