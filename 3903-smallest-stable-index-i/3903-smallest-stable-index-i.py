class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)

        for i in range(n):
            ans = max(nums[0:(i + 1)]) - min(nums[i:n])
            if ans <= k:
                return i
        return -1
        