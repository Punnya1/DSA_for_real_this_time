# class Solution:
#     def secondHighest(self, s: str) -> int:
#         a = set()
#         for i in s:
#             if i.isdigit():
#                 a.add(int(i))
#         if len(a) < 2:
#             return -1
#         return sorted(a)[-2]
# sol = Solution()
# ans = sol.secondHighest("dfa12321afd")
# print(ans)

# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

# Example
# Input: s = "abc1111"
# Output: -1
# Explanation: The digits that appear in s are [1]. There is no second largest digit. 

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x == 0:
#             return True
#         if (x<0 or x%10==0):
#             return False
#         ans = 0
#         while x>ans:
#             ans = ans*10 + x%10
#             x //= 10 
#         if x == ans//10 or x == ans:
#             return True
#         return False


# palindrome = Solution()
# ans = palindrome.isPalindrome(11)
# print(ans)

# class Solution:
#     def reverse(self, x: int) -> int:
#         isNeg = False
#         if x < 0:
#             isNeg = True
#         x = abs(x)
#         ans = 0
#         while x > 0:
#             ans = ans*10 + x %10
#             x //= 10
#         upper_bound = 2**31 - 1
#         lower_bound = -2**31
#         if isNeg:
#             ans = -ans
#         if not lower_bound < ans < upper_bound:
#             return 0
#         return ans
        
# sol = Solution()
# ans = sol.reverse(123)
# print(ans)

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l <= r:
            mid = int(l+ (r-l)/2)
            if nums[mid] < target:
                l = mid +1
            elif nums[mid] > target:
                r = mid -1
            else:
                return mid
        return -1       

abc = Solution()
search = abc.search([-1,0,3,5,9,12], 9)
print(search)