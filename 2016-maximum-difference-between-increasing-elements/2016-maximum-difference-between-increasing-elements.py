class Solution(object):
    def maximumDifference(self, nums):
        n, maxi = len(nums), -1
        for i in range(n):
            for j in range(n):
                if i < j and nums[i] < nums[j]:
                    maxi = max(maxi, nums[j] - nums[i])
        return maxi