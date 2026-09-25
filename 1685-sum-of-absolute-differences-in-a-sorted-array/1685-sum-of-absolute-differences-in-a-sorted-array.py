class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        ans = [0] * n
        pre = []
        k, s = 0, 0
        suf = []
        for i in range(n):
            k += nums[i]
            pre.append(k)
            s += nums[n - i - 1]
            suf.append(s)
        suf = suf[::-1] 

        for i in range(n):
            x = nums[i] * i - (pre[i - 1] if i > 0 else 0)
            y = (suf[i + 1] if i + 1 < n else 0) - nums[i] * (n - i - 1)
            ans[i] = x + y
        return ans
            



            


# class Solution(object):
#     def getSumAbsoluteDifferences(self, nums):
#         n = len(nums)
#         result = [0] * n
#         for i in range(n):
#             val = 0
#             for j in range(n):
#                 if i != j:
#                     val += abs(nums[i] - nums[j])
#             result[i] = val
#         return result
        