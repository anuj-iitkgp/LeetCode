class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        maxi = float("-inf")
        for i in range(len(nums) - 1):
            maxi = max(maxi, nums[i + 1] - nums[i])
        if len(nums) == 1:
            return 0
        return maxi
        