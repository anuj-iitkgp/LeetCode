class Solution(object):
    def stoneGameVIII(self, stones):
        n = len(stones)

        for i in range(1, n):
            stones[i] += stones[i - 1]

        # memo = {}

        # def helper(i):
        #     if i >= n:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     ans = float('-inf')
        #     for j in range(i , n):
        #         ans = max(ans, stones[j] - helper(j + 1))
        #     memo[i] = ans
        #     return ans

        ans = stones[-1]

        for j in range(n - 2, 0, -1):
            ans = max(ans, stones[j] - ans)
        return ans


        

        
        
        