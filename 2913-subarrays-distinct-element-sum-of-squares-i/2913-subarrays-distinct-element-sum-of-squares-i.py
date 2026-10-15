class Solution(object):
    def sumCounts(self, nums):
        s = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                k = len(collections.Counter(nums[i:j+1]))
                s += k * k
        return s
