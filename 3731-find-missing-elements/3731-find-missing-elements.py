class Solution(object):
    def findMissingElements(self, nums):
        max_el = max(nums)
        min_el = min(nums)
        nums_set = set(nums)
        ans = []
        for i in range(min_el, max_el + 1):
            if i not in nums_set:
                ans.append(i)
        
        return ans



        