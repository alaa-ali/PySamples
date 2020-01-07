'''
Diagonal Difference
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
'''
def diagonal_diff(arr):
    rows = len(arr)
    cols = len(arr[0])
    j=0
    sum_left_right = 0
    sum_right_left = 0
    for i in range(0,rows):
        #print(i,j,cols-j-1)
        sum_left_right = sum_left_right + arr[i][j]
        sum_right_left = sum_right_left + arr[i][cols-j-1]
        j=j+1
    
    return abs(sum_right_left - sum_left_right)

#driver code
matA = [[6,1,2,3],
        [4,5,6,7],
        [8,9,10,11],
        [12,8,3,7]]
#Print the absolute difference between the sums of the matrix's two diagonals as a single integer.
print(diagonal_diff(matA))
matB = [[11,2, 4],
        [4, 5, 6],
        [10, 8, -12]]
print(diagonal_diff(matB))


#https://www.hackerrank.com/challenges/diagonal-difference/problem