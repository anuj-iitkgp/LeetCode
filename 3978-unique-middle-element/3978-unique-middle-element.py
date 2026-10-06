class Solution(object):
    def isMiddleElementUnique(self, nums):
        n = len(nums)
        mid = nums[(n - 1) // 2]
        count = 0
        for num in nums:
            if num == mid:
                count += 1
                if count > 1:
                    return False
        return True




        