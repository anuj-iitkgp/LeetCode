class Solution(object):
    def missingMultiple(self, nums, k):

        n = len(nums)
        if k == nums[0] and n == 1:
            return 2 * k
        
        if nums[0] % k == 0 and n == 1:
            return k
        
        ans = {index : value for index, value in enumerate(nums)}
        
        for key, val in ans.items():
            if k * (key + 1) not in ans.values():
                return k * (key + 1)
                break
        return k * (n + 1)
        
        
