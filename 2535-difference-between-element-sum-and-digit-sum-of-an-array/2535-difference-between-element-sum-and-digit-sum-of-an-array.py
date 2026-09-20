class Solution(object):
    def differenceOfSum(self, nums):
        def digitSum(n):
            dsum = 0
            while n:
                dsum += n % 10
                n //= 10
            return dsum

        eSum = sum(nums)
        
        dSum = 0
        for num in nums:
            dSum += digitSum(num)
        
        return abs(eSum - dSum)
        

        