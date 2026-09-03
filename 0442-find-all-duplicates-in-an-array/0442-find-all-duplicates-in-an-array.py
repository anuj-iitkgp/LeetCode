class Solution(object):
    def findDuplicates(self, nums):
        ans = []
        n = len(nums)

        for i in range(n):
            idx = abs(nums[i]) - 1
            nums[idx] = - nums[idx]
            if nums[idx] > 0:
                ans.append(idx + 1)
        
        return ans
            

        
        
        