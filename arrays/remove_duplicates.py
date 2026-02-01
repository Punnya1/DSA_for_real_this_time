from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        for i in range(len(nums)):
            if nums[i] > nums[x]:
                x += 1
                nums[x] = nums[i]
        return x + 1
    
sol = Solution()
ans = sol.removeDuplicates([1,2,3,4,5,5,6,7,7,10,10,12,12])
print(ans)