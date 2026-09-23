class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        mins = float('inf')
        for i in range(n):
            for j in range(i, n):
                if sum(nums[i:j+1]) > 0 and len(nums[i:j+1]) >= l and len(nums[i:j+1]) <= r:
                    mins = min(mins, sum(nums[i:j+1]))
        if mins == float('inf'):
            return -1
        return mins