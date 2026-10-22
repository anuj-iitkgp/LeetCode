class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [-1] * (len(nums))
        def solve(i):
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(nums[i] + solve(i - 2), solve(i - 1))
            return dp[i]
        return solve(len(nums) - 2 + 1)
        