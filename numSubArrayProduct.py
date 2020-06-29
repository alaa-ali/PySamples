def numSubArrayProduct(vec, target):
    if (target<=1): return 0
    result = 0
    product = 1
    left =0
    right =0

    while (right<len(vec)):
        product *= vec[right]
        while(product >= target):
            product /= vec[left]
            left +=1
        result += right - left + 1
        right +=1
    return result

#driver code
a = [10,5,2,6]
print(numSubArrayProduct(a, target =100))

print(numSubArrayProduct(vec = [3,40,2,8,18,1], target =100))

#https://www.youtube.com/watch?v=SxtxCSfSGlo
