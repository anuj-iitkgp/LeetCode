class Solution(object):
    def countBeautifulPairs(self, nums):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        n = len(nums)
        count = 0

        for i in range(n):
            first_digit = int(str(nums[i])[0])
            for j in range(i + 1, n):
                last_digit = nums[j] % 10
                if gcd(first_digit, last_digit) == 1:
                    count += 1
        return count