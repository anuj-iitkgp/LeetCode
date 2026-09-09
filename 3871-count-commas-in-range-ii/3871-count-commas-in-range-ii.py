class Solution(object):
    def countCommas(self, n):
        ans = 0
        k = 1000
        while n >= k:
            ans += n - k + 1
            k *= 10**3
        return ans


            
