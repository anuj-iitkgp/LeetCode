class Solution(object):
    def maxSubsequence(self, nums, k):
        ans = []
        for i, val in enumerate(nums):
            ans.append([val, i])
        ans.sort()
        n = len(ans)
        f = sorted(ans[n - k:], key = lambda x : x[1])
        k = [num[0] for num in f]
        return k