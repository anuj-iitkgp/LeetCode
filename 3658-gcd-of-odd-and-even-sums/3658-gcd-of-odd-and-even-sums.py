class Solution(object):
    def gcdOfOddEvenSums(self, n):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        return gcd(n**2, n**2 + n)