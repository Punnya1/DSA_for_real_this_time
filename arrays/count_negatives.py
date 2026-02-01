# Given an array arr of numbers, return the count of elements strictly less than 0

def count_negatives(arr):
    ans = 0
    for i in arr:
        if i < 0:
            ans += 1
    return ans

answer = count_negatives([-5,6,3,-2,-1,-7])
print(answer)