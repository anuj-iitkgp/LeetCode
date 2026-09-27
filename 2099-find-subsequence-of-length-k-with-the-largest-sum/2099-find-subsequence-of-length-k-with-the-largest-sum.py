class Solution(object):
    def maxSubsequence(self, nums, k):
        ans = [[val, i] for i, val in enumerate(nums)]
        ans.sort()
        n = len(ans)
        f = sorted(ans[n - k:], key = lambda x : x[1])
        return [num[0] for num in f]


# class Solution(object):
#     def maxSubsequence(self, nums, k):
#         ans = []
#         for i, val in enumerate(nums):
#             ans.append([val, i])
#         ans.sort()
#         n = len(ans)
#         f = sorted(ans[n - k:], key = lambda x : x[1])
#         k = [num[0] for num in f]
#         return k