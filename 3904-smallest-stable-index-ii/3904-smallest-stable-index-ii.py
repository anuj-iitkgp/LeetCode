class Solution(object):
    def firstStableIndex(self, nums, k):
        msf = -1
        cSmaIdx = candMax = 0

        for i, x in enumerate(nums):
            msf = max(msf, x)

            if i == cSmaIdx:
                candMax = msf

            if x < candMax - k:
                cSmaIdx = i + 1

        return cSmaIdx if cSmaIdx < len(nums) else -1      



        # min_val = [float('inf')] * (n - 1) + [nums[-1]]

        # for i in range( n - 2, -1, -1):
        #     min_val[i] = min(min_val[i + 1], nums[i])
        
        # max_val = float('-inf')

        # for i in range(n):
        #     max_val = max(max_val, nums[i])
        #     score = max_val - min_val[i]
        #     if score <= k:
        #         return i
        # return -1