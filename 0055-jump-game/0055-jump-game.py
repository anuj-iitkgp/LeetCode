class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # currentReach = 0
        # last = len(nums) - 1
        
        # for i in range(len(nums)):
        #     if i > currentReach:
        #         return False
            
        #     if i + nums[i] > currentReach:
        #         currentReach = i + nums[i]
                
        #     if currentReach >= last:
        #         return True
                
        # return False

        n = len(nums)
        maxJump = 0
        for i in range(n):
            if i > maxJump:
                return False
            maxJump = max(maxJump, i + nums[i])
        return True