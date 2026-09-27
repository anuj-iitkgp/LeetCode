class Solution(object):
    def alternateDigitSum(self, n):
        t, s = 0, str(n)
        for i in range(len(s)):
            if i % 2 == 0:
                t += int(s[i])
            else:
                t -= int(s[i])
        return t