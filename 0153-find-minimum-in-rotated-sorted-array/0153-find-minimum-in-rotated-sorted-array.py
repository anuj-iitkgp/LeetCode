class Solution(object):
    def findMin(self, nums):
        # return min(nums) # T.C. = O(n)

        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low ) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

        



        