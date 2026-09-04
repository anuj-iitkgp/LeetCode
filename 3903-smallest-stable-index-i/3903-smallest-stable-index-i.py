class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        suffix = [0] * n

        mini = float('inf')
        for i in range(n - 1, -1, -1):
            mini = min(mini, nums[i])
            suffix[i] = mini

        maxi = 0
        for i in range(n):
            maxi = max(maxi, nums[i])
            instability_score = maxi - suffix[i]
            if instability_score <= k:
                return i
        
        return -1


# O(n^2)---------------------------------------------

        # for i in range(n):
        #     ans = max(nums[0:(i + 1)]) - min(nums[i:n])
        #     if ans <= k:
        #         return i
        # return -1
       