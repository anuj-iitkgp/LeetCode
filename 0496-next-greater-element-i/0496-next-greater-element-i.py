class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        # Time Complex: O(n * m)
        # res = [-1] * len(nums1)
        # for i in range(len(nums1)):
        #     idx = nums2.index(nums1[i])
        #     for j in range(idx + 1, len(nums2)):
        #         if nums1[i] < nums2[j]:
        #             res[i] = nums2[j]
        #             break
        # return res
        # optimal

        next_greater = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        return [next_greater.get(x, -1) for x in nums1]
            
# Time: O(m + n), Space: O(m)