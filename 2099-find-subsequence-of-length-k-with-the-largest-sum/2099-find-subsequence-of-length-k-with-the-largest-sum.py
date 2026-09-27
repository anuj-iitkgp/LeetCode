class Solution(object):
    def maxSubsequence(self, nums, k):
        # nums.sort()
        # n = len(nums)
        # p = sum(1 for num in nums if num > 0)
        # if p >= k:
        #     return nums[n-k:]
        
        ans = []
        for i, val in enumerate(nums):
            ans.append([val, i])
        ans.sort()
        n = len(ans)
        s = [0] * k
        ans[n - k:]
        f = sorted(ans[n - k:], key = lambda x : x[1])
        k = [num[0] for num in f]
        return k