class Solution(object):
    def missingNumber(self, nums):
        
        n = len(nums)
        sum1 = n * (n + 1) // 2
        diff = sum1 - sum(nums)
        return diff