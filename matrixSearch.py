'''
    Sorted Matrix Search
    v=bK7BCWICvpQ
'''
def matrixSearch(matA, key):
    if (len(matA)==0 or len(matA[0])==0):
        return False
    row = 0 
    col = len(matA[0])-1
    while(row < len(matA) and col >=0):
        if(matA[row][col]==key): return True
        elif(key > matA[row][col]): row = row + 1
        else: col = col - 1
        
    return False
    
#driver code:
matA = [[0,1,2,3],
        [4,5,6,7],
        [8,9,10,11],
        [12,13,14,15]]

print(matrixSearch(matA, 6))
