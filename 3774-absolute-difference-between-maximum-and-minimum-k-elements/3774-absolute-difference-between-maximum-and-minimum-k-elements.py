class Solution(object):
    def absDifference(self, nums, k):
        n = len(nums)
        nums.sort()
        sum1 = sum(nums[:k])
        sum2 = sum(nums[n-k:n])
        return abs(sum1 - sum2)
        