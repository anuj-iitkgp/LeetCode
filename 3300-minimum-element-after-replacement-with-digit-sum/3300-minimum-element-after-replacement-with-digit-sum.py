class Solution(object):
    def minElement(self, nums):
        def digitSum(n):
            t = 0
            while n:
                t += n % 10
                n //= 10
            return t
        return min([digitSum(nums[i]) for i in range(len(nums))])
        # for i in range(len(nums)):
        #     nums[i] = digitSum(nums[i])
        # return min(nums)
        
        