from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for num in nums:
            count[num] += 1
        r,w,b = count
        nums[:r] = [0] * r
        nums[r:w+r] = [1] * w
        nums[w+r:] = [2] * b   
sol = Solution()
nums = [2,0,2,1,1,0]
sol.sortColors(nums)
print(nums)