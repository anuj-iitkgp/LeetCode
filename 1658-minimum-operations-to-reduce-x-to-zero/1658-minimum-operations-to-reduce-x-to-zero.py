class Solution(object):
    def minOperations(self, nums, x):
        target = sum(nums) - x
        
        # If target is 0, we must remove all elements
        if target == 0:
            return len(nums)
        # If target < 0, total sum is less than x, impossible to reach x
        if target < 0:
            return -1
        
        # Map to store prefix_sum -> index
        prefix_map = {0: -1}
        current_sum = 0
        max_len = -1
        
        for i, num in enumerate(nums):
            current_sum += num
            
            # Check if a valid prefix exists such that (current_sum - prefix) == target
            if (current_sum - target) in prefix_map:
                max_len = max(max_len, i - prefix_map[current_sum - target])
            
            # Store the earliest occurrence of current_sum
            if current_sum not in prefix_map:
                prefix_map[current_sum] = i
                
        return len(nums) - max_len if max_len != -1 else -1