class Solution(object):
    def longestConsecutive(self, nums):
        n = len(nums)
        if not nums:
            return 0
        nums.sort()
        max_streak = 1
        current_streak = 1

        for i in range(n - 1):
            if nums[i + 1] == nums[i]:
                continue
            if nums[i + 1] - nums[ i ] == 1:
                current_streak += 1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 1
        return max(max_streak, current_streak)
        