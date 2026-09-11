class Solution(object):
    def removeZeros(self, n):
        return int("".join(x for x in str(n) if x != '0'))
        