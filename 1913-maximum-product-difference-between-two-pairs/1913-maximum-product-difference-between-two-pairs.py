class Solution(object):
    def maxProductDifference(self, nums):
        n = len(nums)
        nums.sort()
        left_pair = nums[0] * nums[1]
        right_pair = nums[-1] * nums[-2]
        ans = abs(left_pair - right_pair)
        return ans