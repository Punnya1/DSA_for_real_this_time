from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter += 1
            if i == 0:
                max_con = max(max_con, counter)
                counter = 0
        return max(max_con, counter)
    
sol = Solution()
ans = sol.findMaxConsecutiveOnes([1,1,0,1,0,1,1,1])
