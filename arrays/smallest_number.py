# Given an arr of numbers, return the smallest number in the array.
# If the array is empty, return null

def find_smallest(arr):
    if arr == []:
        return None
    smallest = float('inf')
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest

ans = find_smallest([])
# ans = find_smallest([1,2,3,4,5,6,-6])
print(ans)