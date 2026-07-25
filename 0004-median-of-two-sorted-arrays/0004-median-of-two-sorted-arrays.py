import numpy as np
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = []
        
        for i in range(len(nums1)):
            nums.append(nums1[i])
        
        for i in range(len(nums2)):
            nums.append(nums2[i])
        
        nums.sort()
        return np.median(nums)
        