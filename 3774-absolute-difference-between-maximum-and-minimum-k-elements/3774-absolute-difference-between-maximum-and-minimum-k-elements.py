class Solution(object):
    def absDifference(self, nums, k):
        n = len(nums)
        nums.sort()
        return abs(sum(nums[:k]) - sum(nums[n-k:n]))
        