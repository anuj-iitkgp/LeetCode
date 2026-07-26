class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        con_ones = 0
        max_con_ones = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                con_ones += 1
                max_con_ones = max(max_con_ones, con_ones)
            else:
                con_ones = 0
        return max_con_ones