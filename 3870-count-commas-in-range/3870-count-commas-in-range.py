class Solution(object):
    def countCommas(self, n):
        
        if n < 1000:
            return 0
        count = 0
        for i in range(1000, 100001):
            if n >= i:
                count += 1
        return count
