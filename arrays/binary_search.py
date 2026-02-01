from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = l+ (r-l)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
    
sol = Solution()
ans = sol.search([4,5,6,8,12,20,29,49,55,335,10000,2020203], target=335)
print(ans)