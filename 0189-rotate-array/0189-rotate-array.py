class Solution(object):
    def rotate(self, nums, k):
        
        n = len(nums)
        
        k %= n
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverse(0, n - 1) # 1. Reverse the whole array
        reverse(0, k - 1) # 2. Reverse the first k elements
        reverse(k, n - 1) # 3. Reverse the remaining n-k elements