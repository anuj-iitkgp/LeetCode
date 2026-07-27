class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        zero_count = 0
        max_len = 0
        
        for right in range(len(nums)):
            # If we encounter a 0, expand our flip count
            if nums[right] == 0:
                zero_count += 1
            
            # Shrink the window from the left if zeros exceed k
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Update the max window length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len