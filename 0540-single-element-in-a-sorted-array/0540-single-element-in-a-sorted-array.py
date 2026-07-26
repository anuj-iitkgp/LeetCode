class Solution(object):
    def singleNonDuplicate(self, nums):
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
        return ans
            
