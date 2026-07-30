class Solution(object):
    def isPowerOfTwo(self, n):
        if (n > 1 and n % 2 == 1) or n == 0 or n  < 0:
            return False
        if n <= 2 :
            return True
        return self.isPowerOfTwo(n // 2)

        
        
        