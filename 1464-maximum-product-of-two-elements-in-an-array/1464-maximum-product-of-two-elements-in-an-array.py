class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        n = len(nums)
        nums.sort()
        return (nums[n - 1] - 1) * (nums[n - 2] - 1)
        Time complexity: O(nlogn)

        """

        first = second = 0
        
        for num in nums:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num
                
        return (first - 1) * (second - 1)