from collections import Counter
class Solution(object):
    def sortByReflection(self, nums):
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append([int(bin(nums[i])[2:][::-1], 2), nums[i]])
        ans.sort()
        for i in range(n):
            nums[i] = ans[i][1]
        return nums
        
        

        