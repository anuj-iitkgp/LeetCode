class Solution(object):
    def findMin(self, nums):
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low ) // 2
            if nums[low] < nums[high]:
                return nums[low]
            if nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]:
                return nums[mid]
            elif nums[mid + 1] < nums[mid] and nums[mid + 1] < nums[high]:
                return nums[mid + 1]
            elif nums[high - 1] < nums[high - 2] and nums[high - 1] < nums[high]:
                return nums[high - 1]
            elif nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] == nums[low] and nums[mid] == nums[high]:
                low += 1
                high -= 1
            else:
                high = mid
        return nums[low]