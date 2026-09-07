from collections import Counter
class Solution(object):
    def checkPrimeFrequency(self, nums):
        def isPrime(n):
            if n <= 1:
                return False
            
            for i in range(2, int(n**(0.5)) + 1):
                if n % i == 0:
                    return False

            return True
        count = Counter(nums)
        for freq in count.values():
            if isPrime(freq):
                return True
        return False
        
        