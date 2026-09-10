class Solution(object):
    def transformArray(self, nums):
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(nums[i] % 2)
        ans.sort()
        return ans