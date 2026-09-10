class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        n = len(nums)
        nums.sort()
        return max(nums[n - 1] + nums[n - 2] - nums[n - 3],nums[n - 1] + nums[n - 2] - nums[0] )
        