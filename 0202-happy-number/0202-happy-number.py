class Solution(object):
    def isHappy(self, n):
        def square(n):
            ans = 0
            while n != 0:
                digit = n % 10
                ans += digit ** 2
                
                n //= 10
            return ans
        
        seen = set()

        while True:
            n = square(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
        