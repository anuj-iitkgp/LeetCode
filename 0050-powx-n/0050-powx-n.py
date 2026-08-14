class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = - n
        
        ans = 1.0
        current_product = x

        while n > 0:
            if n % 2 == 1:
                ans *= current_product
        
            current_product *= current_product 
            n = n // 2
        return ans

# Time (logn), Space O(1)
        
        