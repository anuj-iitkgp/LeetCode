class Solution(object):
    def searchRange(self, nums, target):
        def findBound(isFirst):

            left = 0
            right = len(nums) - 1
            bound = -1

            while left <= right:

                mid = left + (right - left) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    bound = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1

            return bound
        return [findBound(True), findBound(False)]