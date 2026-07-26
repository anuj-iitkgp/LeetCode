
class Solution(object):
    def singleNonDuplicate(self, nums):
        # ans = 0
        # for i in range(len(nums)):
        #     ans ^= nums[i]
        # return ans
        # O(n) time complexity

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
# Ensure mid is even for uniform pair comparison
            if mid % 2 == 1:
                mid -= 1
# If mid and mid+1 match, single element is on the right
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
# Single element is at mid or to the left
                high = mid
        return nums[low]
            
