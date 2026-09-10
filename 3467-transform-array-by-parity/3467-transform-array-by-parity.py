class Solution(object):
    def transformArray(self, nums):
        nums = [1 if x % 2 != 0 else 0 for x in nums]
        nums.sort()
        return nums


        

