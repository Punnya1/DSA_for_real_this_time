class Solution:
    def secondHighest(self, s: str) -> int:
        a = set()
        for i in s:
            if i.isdigit():
                a.add(int(i))
        if len(a) < 2:
            return -1
        return sorted(a)[-2]
sol = Solution()
ans = sol.secondHighest("dfa12321afd")
print(ans)

# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

# Example
# Input: s = "abc1111"
# Output: -1
# Explanation: The digits that appear in s are [1]. There is no second largest digit. 