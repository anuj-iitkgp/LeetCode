class Solution(object):
    def search(self, nums, target):
        n = len(nums)

        if n == 1 and nums[0] != target:
            return -1

        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1