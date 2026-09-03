class Solution(object):
    def findMissingElements(self, nums):
        max_el = max(nums)
        min_el = min(nums)
        nums_set = set(nums)
        return [x for x in range(min_el, max_el + 1) if x not in nums_set]



        