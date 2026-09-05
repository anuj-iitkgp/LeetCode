class Solution(object):
    def firstStableIndex(self, nums, k):
        msf = -1
        cand = cm = 0

        for i, x in enumerate(nums):
            msf = max(msf, x)

            if i == cand:
                cm = msf

            if x < cm - k:
                cand = i + 1

        return cand if cand < len(nums) else -1      



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