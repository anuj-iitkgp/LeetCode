class Solution(object):
    def maxAscendingSum(self, nums):
        def isAsc(arr):
            m = len(arr)
            k = 1 + sum(1 for i in range(1, m) if arr[i - 1] < arr[i])
            return m == k
        s, m = 0, 0
        n = len(nums)
        for i in range(n):
            s = 0
            for j in range(i, n):
                if isAsc(nums[i:j+1]):
                    s += nums[j]
                    m = max(m, s)
        return m

        