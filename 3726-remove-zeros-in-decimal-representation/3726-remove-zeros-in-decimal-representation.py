class Solution(object):
    def removeZeros(self, n):
        str1 = str(n)
        ans = "".join(x for x in str1 if x != '0')
        return int(ans)
        