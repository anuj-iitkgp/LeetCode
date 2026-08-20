class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            for j in range(idx + 1, len(nums2)):
                if nums1[i] < nums2[j]:
                    res[i] = nums2[j]
                    break
        return res
        
            
        