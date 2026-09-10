class Solution(object):
    def canBeIncreasing(self, nums):
        n = len(nums)
        for i in range(n):
            new_nums = nums[:i] + nums[i+1:]
            isInc = True
            for j in range(1, len(new_nums)):
                if new_nums[j - 1] >= new_nums[j]:
                    isInc = False
                    break
            if isInc:
                return True
        return False
        