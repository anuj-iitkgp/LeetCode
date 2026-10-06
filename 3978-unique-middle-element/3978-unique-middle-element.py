class Solution(object):
    def isMiddleElementUnique(self, nums):
        n = len(nums)
        count = collections.Counter(nums)
        mid = nums[(n - 1) // 2]
        if count[mid] != 1:
            return False
        return True
        