class Solution(object):
    def differenceOfSum(self, nums):
        def digitSum(n):
            dsum = 0
            while n:
                dsum += n % 10
                n //= 10
            return dsum
        return abs(sum(nums) - sum(digitSum(num) for num in nums))
        

        