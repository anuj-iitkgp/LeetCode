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



# class Solution(object):
#     def isMiddleElementUnique(self, nums):
#         n = len(nums)
#         count = collections.Counter(nums)
#         mid = nums[(n - 1) // 2]
#         if count[mid] != 1:
#             return False
#         return True
        