class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        is_neg = False
        if x<0:
            is_neg = True
        x = abs(x)
        while x>0:
            ans = ans*10 + x%10
            x //= 10
        if is_neg:
            ans = -ans
        lower_bound = -2**31
        upper_bound = (2**31) - 1
        if not (lower_bound) < ans < upper_bound:
            return 0
        return ans
    
sol = Solution()
print(sol.reverse(-123))