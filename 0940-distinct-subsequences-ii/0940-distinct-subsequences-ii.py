class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7
        cnt = 0
        dp = [0] * 26

        for char in s:
            char = ord(char) -  97
            nex = cnt + 1 - dp[char]
            cnt = (cnt + nex) % MOD
            dp[char] = (dp[char] + nex) % MOD
        return cnt





        # Recusive approach-------------------------
        # def helper(curr, i):
        #     if len(s) == i:
        #         return {curr} if curr else set()

        #     take = helper(curr + s[i], i + 1)
        #     drop = helper(curr, i + 1)
        #     return take.union(drop)
        # return len(helper("", 0))

# Memoization Top-down----------------
        # def helper(curr, i):
        #     memo = {}
        #     if len(s) == i:
        #         return {curr} if curr else set()
            
        #     if (curr, i) in memo:
        #         return memo[(curr, i)]

        #     take = helper(curr + s[i], i + 1)
        #     drop = helper(curr, i + 1)
        #     memo[(curr, i)] = take.union(drop)

        #     return memo[(curr, i)]
        # return len(helper("", 0))


        
