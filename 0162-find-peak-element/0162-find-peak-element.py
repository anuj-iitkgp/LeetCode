class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            # If mid element is strictly less than its right neighbor, 
            # a peak MUST exist on the right side.
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # Otherwise, a peak exists on the left side (including mid).
                right = mid
                
        return left