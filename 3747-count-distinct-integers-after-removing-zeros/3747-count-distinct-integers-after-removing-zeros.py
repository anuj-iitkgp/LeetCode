class Solution(object):
    def countDistinct(self, n):
        ans, p = 0, 1

        while n > 0:
            ld = n % 10
            n //= 10

            if ld == 0:
                ans = 9 * (p - 1) // 8
            else:
                ans += (ld - 1) * p + (p if p > 1 else 1)
            p *= 9
        return ans
        
        