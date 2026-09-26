class Solution(object):
    def maximumLength(self, nums, k):
        n = len(nums)
        # dp[i][j]: max length of good subsequence ending at index i with j transitions
        dp = [[1] * (k + 1) for _ in range(n)]
        max_len = 1

        for i in range(n):
            for j in range(k + 1):
                for prev in range(i):
                    if nums[prev] == nums[i]:
                        dp[i][j] = max(dp[i][j], dp[prev][j] + 1)
                    elif j > 0:
                        dp[i][j] = max(dp[i][j], dp[prev][j - 1] + 1)
                max_len = max(max_len, dp[i][j])

        return max_len