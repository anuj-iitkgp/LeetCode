class Solution(object):
    def rotate(self, nums, k):
        
        n = len(nums)
        nums1 = list(nums)



        for i in range(n):
            new_idx = (i + k) % n
            nums1[new_idx] = nums[i]
        
        nums[:] = nums1
        return nums