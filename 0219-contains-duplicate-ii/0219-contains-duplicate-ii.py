class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False
        
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k :
                return True
            
            seen[num] = i
        return False
        