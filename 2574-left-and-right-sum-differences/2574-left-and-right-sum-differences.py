class Solution(object):
    def leftRightDifference(self, nums):
        n = len(nums)
        l, r = 0, sum(nums)
        ans = [0] * n
        for i in range(n ):
            r -= nums[i]
            ans[i] = abs(l - r)
            l += nums[i]
        return ans



# class Solution(object):
#     def leftRightDifference(self, nums):
        
#         n = len(nums)
#         l, r = 0, 0
#         left_sum = [0]
#         right_sum = [0]
#         for i in range(n - 1):
#             l += nums[i]
#             left_sum.append(l)
#             r += nums[n - i - 1]
#             right_sum.append(r)
#         right_sum = right_sum[::-1]
#         print(left_sum, right_sum)
#         ans = [0] * n
#         for i in range(n):
#             ans[i] = abs(left_sum[i] - right_sum[i])
#         return ans

        