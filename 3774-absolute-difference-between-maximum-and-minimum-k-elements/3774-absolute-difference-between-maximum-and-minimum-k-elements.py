class Solution(object):
    def absDifference(self, nums, k):
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(k):
            ans += - nums[i] + nums[n - i - 1]
        return ans
        