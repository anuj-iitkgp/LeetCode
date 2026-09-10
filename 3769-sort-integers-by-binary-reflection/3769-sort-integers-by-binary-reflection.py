from collections import Counter
class Solution(object):
    def sortByReflection(self, nums):
        n = len(nums)
        num = nums[:]
        ans = []
        for i in range(n):
            num[i] = int(bin(nums[i])[2:][::-1], 2)
            ans.append([num[i], nums[i]])
        
        ans.sort()
        for i in range(n):
            nums[i] = ans[i][1]
        return nums
        
        

        