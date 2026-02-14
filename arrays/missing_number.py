from collections import defaultdict
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        keys = len(nums) + 1
        counter = defaultdict(lambda: 0, {k:0 for k in range(keys)})
        for i in nums:
            counter[i] += 1
        for k,v in counter.items():
            if v == 0:
                return k
sol = Solution()
ans = sol.missingNumber([1,2,0])

        # n = len(nums)
        # total_sum = n* ((n+1)/2)
        # partial_sum = 0
        # for i in nums:
        #     partial_sum += i
        # return int(total_sum - partial_sum)