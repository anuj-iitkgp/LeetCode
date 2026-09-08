class Solution(object):
    def countCommas(self, n):
        
        if n < 1000:
            return 0
        
        return (n - 999)
        # count = 0
        # for i in range(n + 1):

        # # for i in range(1000, 100001):
        # #     if n >= i:
        # #         count += 1
        # return count
