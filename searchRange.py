# First and Last Position of X in Sorted Array
# Facebook Coding Interview Question

def find_first_pos(vec, target):
    n = len(vec)
    first_pos = -1
    low = 0
    high = n-1
    while (low <= high):
        mid = int(low + (high - low) /2)
        if(vec[mid]>= target):
            first_pos = mid
            high = mid - 1
        else: # vec[mid]< target
            low = mid+1
    
    return first_pos

def searchRange(vec, target):
    first = find_first_pos(vec, target)
    last = find_first_pos(vec, target+1) - 1
    if(first <= last):
        return [first, last]
    return [-1, -1]

# driver code//
print(searchRange( [5,7,7,8,8,10], 8))
print(searchRange( [5,7,7,8,8,10], 6))
print(searchRange( [1, 1], 1))
print(searchRange( [4, 5, 4], 4))

#https://www.youtube.com/watch?v=dVXy6hmE_0U
