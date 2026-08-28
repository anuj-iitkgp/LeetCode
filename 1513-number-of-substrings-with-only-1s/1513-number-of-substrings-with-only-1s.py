class Solution(object):
    def numSub(self, s):
        
        count, total = 0, 0
        MOD = 10**9 + 7

        for c in s:
            if c == '1':
                count += 1
            else:
                count = 0
            total = (total + count) % MOD
        return total
        