from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        for i in nums:
            if i != 0:
                nums[x] = i
                x += 1
        for i in range(x, len(nums)):
            nums[i] = 0
        return nums

sol = Solution()
ans = sol.moveZeroes([0,1,3,0,12,55])
print(ans)