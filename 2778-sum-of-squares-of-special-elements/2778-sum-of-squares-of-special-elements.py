class Solution(object):
    def sumOfSquares(self, nums):
        n = len(nums)
        return sum([nums[i - 1]**2 for i in range(1, n + 1) if n % i == 0])
        
        


# class Solution(object):
#     def sumOfSquares(self, nums):
#         n = len(nums)
#         s = 0
#         for i in range(1, n + 1):
#             if n % i == 0:
#                 s += (nums[i - 1])*(nums[i - 1])
#         return s
        