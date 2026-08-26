class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if i < j and nums[i] == nums[j]:
                    count += 1
        return count
