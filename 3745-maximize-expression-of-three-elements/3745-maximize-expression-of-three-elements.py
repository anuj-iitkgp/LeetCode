class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        nums.sort()
        return max(nums[-1] + nums[-2] - nums[-3],nums[-1] + nums[-2] - nums[0] )
        