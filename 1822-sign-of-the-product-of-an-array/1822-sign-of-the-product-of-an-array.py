class Solution(object):
    def arraySign(self, nums):
        
        product = 1
        n = len(nums)

        for i in range(n):
            product *= nums[i]
        
        if product > 0:
            return 1
        elif product < 0:
            return -1
        return 0
        