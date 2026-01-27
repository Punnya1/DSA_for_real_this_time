from typing import List

def gen_row(N):
    ans = []
    val = 1
    ans.append(1)
    for k in range(1,N):
        val = val * (N-k)
        val //= k
        ans.append(val)
    return ans

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1,numRows):
            ans.append(gen_row(i))
        return ans
    
ans = Solution()
result = ans.generate(5)
print(result)