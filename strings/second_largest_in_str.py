class Solution:
    def secondHighest(self, s: str) -> int:
        a = set()
        for i in s:
            if i.isdigit():
                a.add(int(i))
        if len(a) < 2:
            return -1
        sorted(a)
        return a[-2]

sol = Solution()

sol.secondHighest("sjhtz8344")